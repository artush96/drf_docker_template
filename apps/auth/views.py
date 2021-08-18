import logging

from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.contrib.sites.shortcuts import get_current_site
from django.urls import reverse
from django.utils.encoding import smart_bytes, smart_str, DjangoUnicodeDecodeError
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.translation import gettext_lazy as _

from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.views import TokenObtainPairView

from apps.auth.serializers import (ChangePasswordSerializer, PasswordResetEmailSerializer,
                                   SetPasswordSerializer, TokenObtainPairSerializer)
from apps.users.models import User
from snippets.response import response

logger = logging.getLogger(__name__)


class TokenGenerateView(TokenObtainPairView):
    serializer_class = TokenObtainPairSerializer


class ChangePasswordView(generics.UpdateAPIView):
    """Password change view"""
    http_method_names = ['put']
    permission_classes = (IsAuthenticated,)
    serializer_class = ChangePasswordSerializer

    def get_object(self, queryset=None):
        obj = self.request.user
        return obj


class PasswordResetEmailView(generics.GenericAPIView):
    """Password Recovery"""
    http_method_names = ['post']
    permission_classes = ()
    serializer_class = PasswordResetEmailSerializer

    def post(self, request):
        email = request.data.get('email')
        company_id = request.data.get('company_id')
        if User.objects.filter(company_id=company_id, email=email).exists():
            user = User.objects.filter(company_id=company_id).get(email=email)
            uidb64 = urlsafe_base64_encode(smart_bytes(user.id))
            token = PasswordResetTokenGenerator().make_token(user)
            current_site = get_current_site(
                request=request).domain
            relative_link = reverse(
                'password_reset_confirm', kwargs={'uidb64': uidb64, 'token': token}
            )
            absurl = current_site + relative_link
            # send_mail()
<<<<<<< HEAD

            return Response({'success': True, 'message': _('Password reset link sended.')})
=======
            print(absurl)
            return response(
                    status=status.HTTP_200_OK,
                    message='Password reset link sent.'
                )
>>>>>>> 432334e47cc34b2c64ed06bb81847615c877fc46


class PasswordTokenCheckView(APIView):
    permission_classes = ()

    def get(self, request, uidb64, token):
        try:
            id = smart_str(urlsafe_base64_decode(uidb64))
            user = User.objects.get(id=id)
            if not PasswordResetTokenGenerator().check_token(user, token):
                return response(
                        status=status.HTTP_401_UNAUTHORIZED,
                        message='Token is not valid, please request a new one.'
                    )
            return response(
                    status=status.HTTP_200_OK,
                    message='Credentials Valid',
                    data={'uidb64': uidb64, 'token': token}
                )
        except DjangoUnicodeDecodeError as exception:
            raise exception


class SetPasswordView(generics.GenericAPIView):
    serializer_class = SetPasswordSerializer
    permission_classes = ()

    def patch(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        return response(
                status=status.HTTP_200_OK,
                message='Password reset success.'
            )
