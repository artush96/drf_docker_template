from django.contrib import admin

from apps.drivers.models import Car, AttachedFiles, Location


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    pass


@admin.register(AttachedFiles)
class AttachedFilesAdmin(admin.ModelAdmin):
    pass


@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    pass
