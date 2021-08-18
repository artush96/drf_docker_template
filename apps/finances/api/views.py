# import logging

from rest_framework import generics
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.finances.api.serializers import DriversDeptSerializer, DriversRepaymentSerializer, \
    DriversSalarySerializer, CashRegisterSerializer, FinanceListSerializer, FinanceSerializer, \
    FinanceDriverDetailSerializer, CashBoxSerializer
from apps.finances.api.services import get_finance_detail
from apps.users.models import User


# logging.getLogger(__name__)


class FinanceView(APIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = FinanceSerializer

    def get(self, request, *args, **kwargs):
        data = get_finance_detail(request)
        return Response(self.serializer_class(data).data)


class FinanceListView(generics.ListAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = FinanceListSerializer
    queryset = User.drivers.all()


class FinanceDriverDetailView(generics.RetrieveAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = FinanceDriverDetailSerializer
    lookup_url_kwarg = 'id'
    queryset = User


class DriverDeptCreateView(generics.CreateAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = CashBoxSerializer


class DriverDeptListView(generics.ListAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = CashBoxSerializer

    def get_queryset(self):
        driver = get_object_or_404(User, id=self.kwargs.get('id'))
        return driver.transfers_in.filter()


class DriverDeptView(generics.RetrieveUpdateAPIView):
    http_method_names = ['get', 'put']
    permission_classes = (IsAuthenticated,)
    serializer_class = CashBoxSerializer
    lookup_url_kwarg = 'id'


class DriversRepaymentCreateView(generics.CreateAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = CashBoxSerializer


class DriversRepaymentListView(generics.ListAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = CashBoxSerializer

    def get_queryset(self):
        driver = get_object_or_404(User, id=self.kwargs.get('id'))
        return driver.transfers_out.all()


class DriversRepaymentView(generics.RetrieveUpdateAPIView):
    http_method_names = ['get', 'put']
    permission_classes = (IsAuthenticated,)
    serializer_class = CashBoxSerializer
    lookup_url_kwarg = 'id'


class DriversSalaryCreateView(generics.CreateAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = DriversSalarySerializer


class DriversSalaryView(generics.RetrieveUpdateAPIView):
    http_method_names = ['get', 'put']
    permission_classes = (IsAuthenticated,)
    serializer_class = DriversSalarySerializer
    lookup_url_kwarg = 'id'


class DriverSalaryListView(generics.ListAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = DriversSalarySerializer

    def get_queryset(self):
        driver = get_object_or_404(User, id=self.kwargs.get('id'))
        return driver.transferred_salaries


class CashRegisterCreateView(generics.CreateAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = CashRegisterSerializer


class CashRegisterView(generics.RetrieveUpdateAPIView):
    http_method_names = ['get', 'put']
    permission_classes = (IsAuthenticated,)
    serializer_class = CashRegisterSerializer
    lookup_url_kwarg = 'id'
