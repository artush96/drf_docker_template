from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics, status

from apps.choices.api.serializers import CarBrandSerializer, CarModelSerializer
from apps.choices.enums import DeviceEnum, OrderStatusEnum, PaymentTypeEnum, CurrencyEnum, CashTypeEnum
from apps.choices.models import CarBrand, CarModel


enum_class = {
    'device': DeviceEnum,
    'order_status': OrderStatusEnum,
    'payment_type': PaymentTypeEnum,
    'currency': CurrencyEnum,
    'cash_type': CashTypeEnum,
}


class EnumListView(APIView):

    def get(self, request, *args, **kwargs):
        return Response(enum_class.keys())


class EnumView(APIView):

    def get(self, request, *args, **kwargs):
        enums = [{'value': i[0], 'name': i[1]} for i in enum_class[kwargs.get('enum')].choices]
        return Response(enums)


class CarBrandListView(generics.ListAPIView):
    serializer_class = CarBrandSerializer

    queryset = CarBrand


class CarModelListView(generics.ListAPIView):
    serializer_class = CarModelSerializer

    model = CarModel

    def get_queryset(self):
        car_brand = get_object_or_404(CarBrand, id=self.kwargs.get('id'))
        return self.model.objects.filter(brand=car_brand)
