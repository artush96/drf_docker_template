from rest_framework import serializers

from apps.choices.models import CarBrand, CarModel


class CarBrandSerializer(serializers.ModelSerializer):

    class Meta:
        model = CarBrand
        fields = ('id', 'name')


class CarModelSerializer(serializers.ModelSerializer):
    brand = CarBrandSerializer()

    class Meta:
        model = CarModel
        fields = ('id', 'name', 'brand')
