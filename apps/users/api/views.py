from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from apps.users.api.serializers import UserSerializer
from apps.users.models import User


class UserListView(generics.ListAPIView):
    """User list view"""
    permission_classes = (IsAuthenticated,)
    serializer_class = UserSerializer
    queryset = User.objects.all()
