from django.contrib import admin

from apps.customers.models import Customer, Address


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    search_fields = ('id', 'phone')


@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    search_fields = ('id', 'customer__name', 'address')
