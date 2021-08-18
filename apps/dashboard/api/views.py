from django.db.models import Count, Sum
from rest_framework.filters import OrderingFilter
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView

from apps.dashboard.api.serializers import DashboardSerializer, TopDriversSerializer
from apps.dashboard.api.services import get_dashboard_detail
from apps.users.models import User


class DashboardView(APIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = DashboardSerializer

    def get(self, request, *args, **kwargs):
        data = get_dashboard_detail(request)
        return Response(self.serializer_class(data).data)


class TopDriversView(ListAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = TopDriversSerializer
    filter_backends = [OrderingFilter]

    ordering_fields = ['id', 'first_name', 'order_count', 'delay_duration']

    model = User

    def get_queryset(self, *args, **kwargs):
        queryset = self.model.drivers.filter(company_id=self.kwargs.get('company_id'))\
            .annotate(order_count=Count('orders'), delay_duration=Sum('orders__duration'))
        return queryset
