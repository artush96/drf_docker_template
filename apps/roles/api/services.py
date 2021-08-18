from django.contrib.auth.models import Permission

from rest_framework.generics import get_object_or_404

from apps.roles.models import Roles


def role_management(self, request, **kwargs):
    serializer = self.serializer_class(request.data)
    if request.method == 'PUT':
        group = get_object_or_404(Roles, id=kwargs.get('id'))
    else:
        group = Roles.objects.create(name=serializer.data.get('name'), company_id=kwargs.get('company_id'))

    permissions = []
    for perm in serializer.data['roles']:
        permission = Permission.objects.filter(
            content_type__model=perm['model_name'],
            codename__in=[str(j) + '_%s' % perm['model_name'] for j in perm['permissions']])
        for i in permission:
            permissions.append(i)
    if request.method == 'PUT':
        group.permissions.clear()
    group.permissions.add(*permissions)
    group.save()
