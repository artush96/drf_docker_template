from django.contrib.auth import get_user_model, authenticate
from django.contrib.auth.models import update_last_login
from django.contrib.auth.password_validation import validate_password
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.utils.http import urlsafe_base64_decode
from rest_framework import serializers
from django.utils.translation import gettext_lazy as _
from rest_framework.exceptions import AuthenticationFailed
from rest_framework_simplejwt.serializers import PasswordField
from rest_framework_simplejwt.settings import api_settings
from rest_framework_simplejwt.tokens import RefreshToken

from apps.users.models import User, UserLoginIp
from snippets.utils.ip import get_client_ip


class TokenObtainSerializer(serializers.Serializer):
    username_field = get_user_model().USERNAME_FIELD

    default_error_messages = {
        'no_active_account': _('No active account found with the given credentials')
    }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields[self.username_field] = serializers.CharField()
        self.fields['company_id'] = PasswordField()
        self.fields['password'] = PasswordField()

    def validate(self, attrs):
        authenticate_kwargs = {
            self.username_field: attrs[self.username_field],
            'company_id': attrs['company_id'],
            'password': attrs['password'],
        }
        try:
            authenticate_kwargs['request'] = self.context['request']
        except KeyError:
            pass

        self.user = authenticate(**authenticate_kwargs)

        if not api_settings.USER_AUTHENTICATION_RULE(self.user):
            raise AuthenticationFailed(
                self.error_messages['no_active_account'],
                'no_active_account',
            )

        return {}

    @classmethod
    def get_token(cls, user):
        raise NotImplementedError('Must implement `get_token` method for `TokenObtainSerializer` subclasses')


class TokenObtainPairSerializer(TokenObtainSerializer):
    @classmethod
    def get_token(cls, user):
        return RefreshToken.for_user(user)

    def validate(self, attrs):
        data = super().validate(attrs)

        refresh = self.get_token(self.user)

        data['refresh'] = str(refresh)
        data['access'] = str(refresh.access_token)

        if api_settings.UPDATE_LAST_LOGIN:
            update_last_login(None, self.user)
        print(self.context['request'])

        ip = get_client_ip(self.context['request'])

        UserLoginIp.objects.update_or_create(user=self.user, ip=ip)

        return data


class ResetPasswordSerializer(serializers.Serializer):
    new_password1 = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    new_password2 = serializers.CharField(write_only=True, required=True)

    def validate(self, data):
        if self.context['request'].data['new_password1'] != self.context['request'].data['new_password2']:
            raise serializers.ValidationError({"new_password2": _("Password fields didn't match.")})

        return data

    def update(self, instance, validated_data):

        instance.set_password(validated_data['new_password1'])
        instance.save()

        return instance


class ChangePasswordSerializer(ResetPasswordSerializer):
    old_password = serializers.CharField(write_only=True, required=True)

    def validate_old_password(self, value):
        user = self.context['request'].user
        if not user.check_password(value):
            raise serializers.ValidationError({"old_password": _("Old password is not correct")})
        return value


class PasswordResetEmailSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True, write_only=True)
    company_id = serializers.IntegerField(required=True)


class SetPasswordSerializer(serializers.Serializer):
    new_password1 = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    new_password2 = serializers.CharField(write_only=True, required=True)
    token = serializers.CharField(min_length=1, write_only=True, required=True)
    uidb64 = serializers.CharField(min_length=1, write_only=True, required=True)

    class Meta:
        fields = ['password', 'token', 'uidb64']

    def validate(self, attrs):
        if attrs('new_password1') != attrs('new_password2'):
            raise serializers.ValidationError({"new_password2": _("Password fields didn't match.")})
        try:
            password = attrs.get('password')
            token = attrs.get('token')
            uidb64 = attrs.get('uidb64')

            id = urlsafe_base64_decode(uidb64)
            user = User.objects.get(id=id)

            if not PasswordResetTokenGenerator().check_token(user, token):
                raise AuthenticationFailed(_('The reset link is invalid.'), 401)
            user.set_password(password)
            user.save()
        except Exception:
            raise AuthenticationFailed(_('The reset link is invalid.'), 401)
        return super().validate(attrs)

