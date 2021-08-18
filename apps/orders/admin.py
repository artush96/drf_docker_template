from django.contrib import admin
from simple_history.admin import SimpleHistoryAdmin

from apps.orders.models import Order, OrderActivity, OrderDispatcherActivity, OrderDriverActivity


@admin.register(Order)
class OrderAdmin(SimpleHistoryAdmin):
    pass
    # autocomplete_fields = ('driver', 'replaced_driver', 'customer', 'address')
    # raw_id_fields = ('customer',)


@admin.register(OrderActivity)
class OrderActivityAdmin(SimpleHistoryAdmin):
    pass


@admin.register(OrderDispatcherActivity)
class OrderDispatcherActivityAdmin(admin.ModelAdmin):
    pass


@admin.register(OrderDriverActivity)
class OrderDriverActivityAdmin(admin.ModelAdmin):
    list_display = ['id', 'driver', 'dispatcher', 'activity_type']
