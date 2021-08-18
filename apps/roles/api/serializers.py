from rest_framework import serializers


class PermissionSerializer(serializers.Serializer):
    model_name = serializers.CharField()
    permissions = serializers.ListField()


class GroupCreateSerializer(serializers.Serializer):
    name = serializers.CharField()
    roles = PermissionSerializer(many=True)


class GroupSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField()
    members_count = serializers.SerializerMethodField(method_name='get_members_count')
    permissions = serializers.SerializerMethodField(method_name='get_permissions')
    updated = serializers.DateTimeField()
    created = serializers.DateTimeField()

    @staticmethod
    def get_permissions(obj):
        model_names = set()
        data = []
        for j in obj.permissions.all():
            model_names.add(j.codename.split('_')[1])

        for i in model_names:
            res_permissions = []

            for perm in obj.permissions.all():

                if perm.codename.split('_')[1] == i:
                    res_permissions.append(perm.codename.split('_')[0])

            data.append(
                {
                    'model_name': i,
                    'permissions': res_permissions
                }
            )

        return PermissionSerializer(data, many=True).data

    @staticmethod
    def get_members_count(obj):
        return obj.user_set.count()



