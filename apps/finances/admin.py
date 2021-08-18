from django.contrib import admin

from apps.finances.models import DriversDept, DriversRepayment, CashBox


@admin.register(DriversDept)
class DriversDeptAdmin(admin.ModelAdmin):
    pass


@admin.register(DriversRepayment)
class DriversRepaymentAdmin(admin.ModelAdmin):
    pass


@admin.register(CashBox)
class CashBoxAdmin(admin.ModelAdmin):
    pass
