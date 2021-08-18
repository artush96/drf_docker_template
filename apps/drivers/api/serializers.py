from rest_framework import serializers

from apps.drivers.models import DriverRating, Car
from apps.orders.models import OrderActivity
from apps.users.models import User
from apps.users.api.serializers import AttachedFilesSerializer
from apps.choices.api.serializers import CarModelSerializer


class CarSerializer(serializers.ModelSerializer):
    model = CarModelSerializer()

    class Meta:
        model = Car
        fields = ('model', 'plate')


class DriverProfileSerializer(serializers.ModelSerializer):
    car = CarSerializer()
    balance = serializers.IntegerField()

    class Meta:
        model = User
        fields = (
            'id', 'username', 'first_name', 'last_name', 'full_name',
            'phone', 'image', 'car', 'balance'
        )


class DriverSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name', 'phone', 'image')


class DriverCreateSerializer(serializers.ModelSerializer):
    car_model = serializers.IntegerField(required=True)
    car_plate = serializers.CharField(required=True)
    device_platform = serializers.CharField(required=True)
    attach_file = serializers.FileField()

    class Meta:
        model = User
        fields = (
            'phone', 'first_name', 'last_name',
            'email', 'car_model', 'car_plate',
            'device_platform', 'note', 'attach_file'
        )
        extra_kwargs = {
            'first_name': {'required': True}, 'last_name': {'required': True},
            'phone': {'required': True}, 'email': {'required': True}
        }


class DriversListSerializer(serializers.ModelSerializer):
    rating = serializers.FloatField()

    class Meta:
        model = User
        fields = (
            'id', 'phone', 'first_name', 'last_name',
            'full_name', 'email', 'rating'
        )


class DriverDetailSerializer(serializers.ModelSerializer):
    attached_files = serializers.SerializerMethodField('get_attached_files')
    image = serializers.SerializerMethodField('get_image')

    class Meta:
        model = User
        fields = (
            'image', 'phone', 'first_name', 'last_name', 'date_joined',
            'email', 'attached_files',
            # 'car',
        )

    @staticmethod
    def get_attached_files(obj):
        return AttachedFilesSerializer(obj.files.all(), many=True).data

    @staticmethod
    def get_image(obj):
        return obj.image.url


class DriverActivitySerializer(serializers.ModelSerializer):
    order_address = serializers.SerializerMethodField('get_order_address')

    class Meta:
        model = OrderActivity
        fields = (
            'order_id', 'order_status', 'created', 'order_address'
        )

    @staticmethod
    def get_order_address(obj):
        return obj.order.address.address

    @staticmethod
    def get_order_id(obj):
        return obj.order.id


class RatingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = DriverRating
        fields = (
            'id', 'driver', 'order', 'rating', 'comment', 'created'
        )
