from django.db.models import Avg, Sum
from rest_framework import generics, status
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.drivers.api.serializers import (
    DriverCreateSerializer, DriversListSerializer, DriverDetailSerializer,
    RatingsSerializer, DriverActivitySerializer, DriverProfileSerializer
)
from apps.drivers.models import Car, AttachedFiles
from apps.orders.api.serializers import OrderListSerializer
from apps.orders.models import OrderActivity
from apps.users.models import User
from snippets.utils.passwords import generate_password


class ProfileView(APIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = DriverProfileSerializer
    model = User

    def get(self, *args, **kwargs):
        return Response(self.serializer_class(self.get_queryset()).data)

    def get_queryset(self):
        queryset = self.model.drivers.filter(
            company_id=self.kwargs.get('company_id'),
            id=self.kwargs.get('id')
        ).annotate(balance=Sum('transfers_in__amount')).last()
        return queryset


class DriverCreateView(generics.CreateAPIView):
    """Driver list view"""

    permission_classes = (IsAuthenticated,)
    serializer_class = DriverCreateSerializer

    def post(self, request, *args, **kwargs):
        data = self.serializer_class(request.data).data

        password = generate_password()

        driver = User.objects.create(
            company_id=kwargs.get('company_id'),
            is_driver=True,
            phone=data.get('phone'),
            first_name=data.get('first_name'),
            last_name=data.get('last_name'),
            email=data.get('email'),
            note=data.get('note'),
            device_platform=data.get('device_platform'),
            password=password,
            initial_password=password
        )

        car = Car.objects.create(
            driver=driver,
            plate=data.get('car_plate'),
            model_id=data.get('car_model')
        )
        AttachedFiles.objects.create(
            car=car,
            file=data.get('attach_file')
        )
        return Response(status=status.HTTP_201_CREATED)


class DriversListView(generics.ListAPIView):
    """Driver list view"""

    permission_classes = (IsAuthenticated,)
    serializer_class = DriversListSerializer
    filter_backends = [SearchFilter, OrderingFilter]

    ordering_fields = ['id', 'first_name']
    search_fields = ['phone']
    model = User

    def get_queryset(self, *args, **kwargs):
        queryset = self.model.drivers.filter(company_id=kwargs.get('company_id'))\
            .annotate(rating=Avg('ratings'))
        return queryset


class DriverDetailView(generics.RetrieveAPIView):
    """Driver detail view"""

    permission_classes = (IsAuthenticated,)
    serializer_class = DriverDetailSerializer
    lookup_url_kwarg = 'id'
    queryset = User


class DriverOrdersView(generics.ListAPIView):
    """Driver orders list view"""

    permission_classes = (IsAuthenticated,)
    serializer_class = OrderListSerializer
    filter_backends = [OrderingFilter]

    ordering_fields = ['id', 'first_name']

    def get_queryset(self):
        driver = get_object_or_404(User, id=self.kwargs.get('id'))
        return driver.orders.all()


class DriverActivityView(generics.ListAPIView):
    """Driver activities list view"""

    permission_classes = (IsAuthenticated,)
    serializer_class = DriverActivitySerializer
    filter_backends = [OrderingFilter]

    ordering_fields = ['id', 'first_name']

    def get_queryset(self):
        driver = get_object_or_404(User, id=self.kwargs.get('id'))
        queryset = OrderActivity.objects.filter(order__driver=driver)
        return queryset


class DriverRatingsView(generics.ListAPIView):
    """Driver ratings list view"""

    permission_classes = (IsAuthenticated,)
    serializer_class = RatingsSerializer
    filter_backends = [OrderingFilter]

    ordering_fields = ['id', 'first_name']

    def get_queryset(self):
        driver = get_object_or_404(User, id=self.kwargs.get('id'))
        return driver.ratings.all()


class CreateDriverRatingView(generics.CreateAPIView):
    """Driver ratings list view"""

    permission_classes = (IsAuthenticated,)
    serializer_class = RatingsSerializer
