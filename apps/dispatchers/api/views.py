from rest_framework import generics
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated

from apps.dispatchers.api.serializers import DispatcherCreateSerializer, DispatcherSerializer, \
    DispatcherActivitySerializer
from apps.orders.models import OrderDriverActivity
from apps.users.models import User


class DispatcherCreateView(generics.CreateAPIView):
    """Dispatcher create view"""

    permission_classes = (IsAuthenticated,)
    serializer_class = DispatcherCreateSerializer


class DispatcherListView(generics.ListAPIView):
    """Dispatcher list view"""

    permission_classes = (IsAuthenticated,)
    serializer_class = DispatcherSerializer
    filter_backends = [SearchFilter, OrderingFilter]

    ordering_fields = ['id', 'first_name']
    search_fields = ['phone']
    model = User

    def get_queryset(self, *args, **kwargs):
        queryset = self.model.dispatchers.filter(company_id=kwargs.get('company_id'))
        return queryset


class DispatcherDetailView(generics.RetrieveAPIView):
    """Dispatcher detail view"""

    permission_classes = (IsAuthenticated,)
    serializer_class = DispatcherSerializer
    lookup_url_kwarg = 'id'
    queryset = User


class DispatcherActivityView(generics.ListAPIView):
    """Dispatcher activity list view"""

    permission_classes = (IsAuthenticated,)
    serializer_class = DispatcherActivitySerializer
    filter_backends = [OrderingFilter]

    ordering_fields = ['id', 'first_name']

    def get_queryset(self):
        dispatcher = get_object_or_404(User, id=self.kwargs.get('id'))
        queryset = OrderDriverActivity.objects.filter(dispatcher=dispatcher)
        return queryset
