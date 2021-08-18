from django.contrib import admin

from apps.settings.models import Terms, GeneralSettings, Notification


@admin.register(Terms)
class TermsAdmin(admin.ModelAdmin):
    pass


@admin.register(GeneralSettings)
class GeneralSettingsAdmin(admin.ModelAdmin):
    pass


@admin.register(Notification)
class NotificationAdmin(admin.ModelAdmin):
    pass
