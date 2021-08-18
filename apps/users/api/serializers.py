import os

from rest_framework import serializers

from apps.users.models import User, AttachedFiles


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'username', 'first_name')


class AttachedFilesSerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField('get_file_name')

    class Meta:
        model = AttachedFiles
        fields = ('file', 'name')

    @staticmethod
    def get_file_name(obj):
        return str(os.path.basename(obj.file.url))


