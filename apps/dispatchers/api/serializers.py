from rest_framework import serializers

from apps.orders.models import OrderDriverActivity
from apps.users.api.serializers import AttachedFilesSerializer
from apps.users.models import User


class DispatcherCreateSerializer(serializers.ModelSerializer):
    role = serializers.IntegerField(required=True)

    class Meta:
        model = User
        fields = ('company_id', 'first_name', 'last_name', 'phone', 'email', 'note', 'role')
        extra_kwargs = {
            'first_name': {'required': True}, 'last_name': {'required': True},
            'phone': {'required': True}, 'email': {'required': True},
            'note': {'required': True}, 'role': {'required': True}}


class DispatcherSerializer(serializers.ModelSerializer):
    role = serializers.SerializerMethodField('get_role')
    last_activity = serializers.SerializerMethodField('get_last_activity')
    attached_files = serializers.SerializerMethodField('get_attached_files')
    image = serializers.SerializerMethodField('get_image')

    class Meta:
        model = User
        fields = (
            'id', 'full_name', 'first_name', 'last_name', 'email',
            'phone', 'date_joined', 'role', 'last_activity', 'image', 'attached_files'
        )

    @staticmethod
    def get_role(obj):
        return obj.groups.last().name if obj.groups.last() else None

    @staticmethod
    def get_last_activity(obj):
        return obj.dispatcher_activity.last().created if obj.dispatcher_activity.last() else None

    @staticmethod
    def get_attached_files(obj):
        return AttachedFilesSerializer(obj.files.all(), many=True).data

    @staticmethod
    def get_image(obj):
        return obj.image.url


class DispatcherDetailSerializer(serializers.ModelSerializer):
    role = serializers.SerializerMethodField('get_role')
    last_activity = serializers.SerializerMethodField('get_last_activity')

    class Meta:
        model = User
        fields = (
            'id', 'full_name', 'first_name', 'last_name', 'email',
            'phone', 'date_joined', 'role', 'last_activity'
        )

    @staticmethod
    def get_role(obj):
        return obj.groups.last().name if obj.groups.last() else None

    @staticmethod
    def get_last_activity(obj):
        return obj.dispatcher_activity.last().created if obj.dispatcher_activity.last() else None


class DispatcherActivitySerializer(serializers.Serializer):
    name = serializers.CharField()
    value = serializers.CharField()

    # @staticmethod
    # def get_statuses():





