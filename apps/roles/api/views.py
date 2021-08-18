from rest_framework import generics, status
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from apps.roles.api.serializers import GroupCreateSerializer, GroupSerializer
from apps.roles.api.services import role_management
from apps.roles.models import Roles
from snippets.permissions import IsSuperUser


class GroupView(generics.GenericAPIView):
    permission_classes = (IsAuthenticated, IsSuperUser)
    serializer_class = GroupCreateSerializer

    def get(self, request, *args, **kwargs):
        self.serializer_class = GroupSerializer
        queryset = Roles.objects.filter(company_id=kwargs.get('company_id'))
        return Response(self.serializer_class(queryset, many=True).data)

    def post(self, request, **kwargs):
        role_management(self, request, **kwargs)
        return Response(status=status.HTTP_200_OK)

    def put(self, request, **kwargs):
        role_management(self, request, **kwargs)
        return Response(status=status.HTTP_200_OK)

    def delete(self, request, **kwargs):
        get_object_or_404(Roles, id=kwargs.get('id')).delete()
        return Response(status=status.HTTP_204_NO_CONTENT)





