from rest_framework import serializers

from apps.settings.models import Notification
from apps.settings.models import GeneralSettings, Terms


class GeneralSettingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = GeneralSettings
        fields = (
            # 'id',
            'currency', 'driver_arrived_radius',
            'driver_office_radius', 'return_countdown_break_duration'
        )


class TermsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Terms
        fields = (
            # 'id',
            'terms_and_conditions', 'privacy_policy'
        )


class NotificationsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = (
            # 'id',
            'event', 'sms', 'email'
        )
