from rest_framework import generics, status
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.customers.models import Address, Customer
from apps.drivers.api.services import get_auto_assign_driver
from apps.orders.api.serializers import (
    OrserCreateSerializer, OrderListSerializer, OrderDetailSerializer, OrderDetailHistorySerializer,
)
from apps.orders.models import Order
from snippets.response import response
from snippets.utils.datetime import utc_now
from snippets.filters import ModelFilterBackend, LimitOffsetPagination


class OrderCreateView(APIView):
    """Order Create View"""

    permission_classes = (IsAuthenticated,)
    serializer_class = OrserCreateSerializer

    def post(self, request, *args, **kwargs):
        data = self.serializer_class(request.data).data

        customer = Customer.objects.get_or_create(
            first_name=data.get('full_name').split(' ')[0],
            last_name=data.get('full_name').split(' ')[1],
            email=data.get('email'),
            phone=data.get('phone'),
        )

        address = Address.objects.get_or_create(
            customer=customer[0],
            address=data.get('address'),
            apartment=data.get('apartment'),
            entrance=data.get('entrance'),
            floor=data.get('floor'),
        )

        driver_id = request.data.get('driver')
        if driver_id:
            driver = driver_id
        else:
            driver = get_auto_assign_driver().id

        Order.objects.create(
            company_id=kwargs.get('company_id'),
            driver_id=driver,
            payment_type=data.get('payment_type'),
            customer=customer[0],
            first_name=data.get('full_name').split(' ')[0],
            last_name=data.get('full_name').split(' ')[1],
            phone=data.get('phone'),
            price=data.get('price'),
            order_id=data.get('order_id'),
            comment=data.get('comment'),
            address=address[0],
            remind_me=data.get('remind_me'),
            remind_me_minutes=data.get('remind_me_minutes'),
            start_datetime=data.get('start_datetime')
        )

        return Response(status=status.HTTP_201_CREATED)


class OrderListView(generics.ListAPIView):
    """Order list view"""

    permission_classes = (IsAuthenticated,)
    serializer_class = OrderListSerializer
    # pagination_class = LimitOffsetPagination
    filter_backends = [ModelFilterBackend, SearchFilter, OrderingFilter]

    filter_params = {
        'created__date__gte': 'created__date__gte',
        'created__date__lt': 'created__date__lt',
        'payment_type': 'payment_type',
        'order_status': 'order_status',
    }

    ordering_fields = ['id', 'first_name', 'price']
    search_fields = ['phone', 'first_name', 'last_name']
    model = Order

    def get_queryset(self, *args, **kwargs):
        queryset = self.model.objects.filter(company_id=kwargs.get('company_id'))
        return queryset


class OrderDetailView(generics.RetrieveAPIView):
    """Order detail view"""

    permission_classes = (IsAuthenticated,)
    serializer_class = OrderDetailSerializer
    lookup_url_kwarg = 'id'

    def get_queryset(self, *args, **kwargs):
        queryset = Order.objects.filter(company_id=kwargs.get('company_id'))
        return queryset


class OrderCancelView(APIView):
    """Order cancel view"""

    permission_classes = (IsAuthenticated,)
    model = Order

    def delete(self, request, *args, **kwargs):
        order = get_object_or_404(self.model, id=self.kwargs.get('id'))
        if not order.canceled:
            order.canceled = True
            order.cancel_datetime = utc_now()
            order.save()
        else:
            return response(
                status=status.HTTP_200_OK,
                message='Order already canceled.'
            )
        return response(status=status.HTTP_204_NO_CONTENT)


class OrderDetailHistoryView(generics.RetrieveAPIView):
    """Order detail view"""

    permission_classes = (IsAuthenticated,)
    serializer_class = OrderDetailHistorySerializer
    lookup_url_kwarg = 'id'
    queryset = Order





