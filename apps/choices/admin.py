from django.contrib import admin

from apps.choices.models import CarBrand, CarModel


@admin.register(CarBrand)
class CarBrandAdmin(admin.ModelAdmin):
    pass


@admin.register(CarModel)
class CarModelAdmin(admin.ModelAdmin):
    pass
