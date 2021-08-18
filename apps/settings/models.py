from django.db import models
from django.utils.translation import gettext_lazy as _
from simple_history.models import HistoricalRecords

from apps.choices.enums import CurrencyEnum
from snippets.models.abstracts import LastModMixin
from snippets.models.creating_limit import validate_only_count_instance


class GeneralSettings(LastModMixin):
    """General settings model"""
    company = models.OneToOneField('company.Company', on_delete=models.CASCADE, related_name='settings')
    currency = models.CharField(
        max_length=5, choices=CurrencyEnum.choices,
        default=CurrencyEnum.AMD, verbose_name=_('Currency')
    )
    driver_arrived_radius = models.FloatField(default=0.2, verbose_name=_('Driver arrived radius'))
    driver_office_radius = models.FloatField(default=0.1, verbose_name=_('Driver office radius'))
    return_countdown_break_duration = models.IntegerField(default=10, verbose_name=_('Return countdown break duration'))

    history = HistoricalRecords()

    class Meta:
        verbose_name = 'General settings'
        verbose_name_plural = 'General settings'

    # def clean(self):
    #     validate_only_count_instance(self, 1)

    def __str__(self):
        return '%s | %s' % (self.currency, self.company.name)


class Terms(LastModMixin):
    """Terms and Privacy Policy"""
    company = models.OneToOneField('company.Company', on_delete=models.CASCADE, related_name='terms')
    terms_and_conditions = models.TextField(max_length=5000, blank=True, verbose_name=_('Terms and Conditions'))
    privacy_policy = models.TextField(max_length=5000, blank=True, verbose_name=_('Privacy Policy'))

    history = HistoricalRecords()

    class Meta:
        verbose_name = 'Terms and Privacy Policy'
        verbose_name_plural = 'Terms and Privacy Policy'

    # def clean(self):
    #     validate_only_count_instance(self, 1)

    def __str__(self):
        return '%s | %s' % (self.id, self.company.name)


class Notification(LastModMixin):
    """Notification settings model"""
    company = models.OneToOneField('company.Company', on_delete=models.CASCADE, related_name='notification')
    event = models.CharField(max_length=50, verbose_name=_('Event'))
    sms = models.BooleanField(default=False, verbose_name=_('SMS'))
    email = models.BooleanField(default=False, verbose_name=_('Email'))

    history = HistoricalRecords()

    class Meta:
        verbose_name = 'Notification'
        verbose_name_plural = 'Notifications'

    # def clean(self):
    #     validate_only_count_instance(self, 1)

    def __str__(self):
        return '%s | %s | %s' % (self.event, self.sms, self.email)


class DriverSalary(LastModMixin):
    pass


# class ExtraPayment(LastModMixin):
#     pass
