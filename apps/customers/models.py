from django.core.validators import EmailValidator
from django.db import models
from django.utils.translation import gettext_lazy as _
from simple_history.models import HistoricalRecords

from snippets.models.abstracts import LastModMixin


class Customer(LastModMixin):
    """Customer Model"""
    first_name = models.CharField(max_length=50, verbose_name=_('First Name'))
    last_name = models.CharField(max_length=50, verbose_name=_('Last Name'))
    email = models.EmailField(verbose_name=_('Email'), validators=[EmailValidator])
    phone = models.CharField(max_length=50, verbose_name=_('Phone'))
    note = models.CharField(max_length=300, verbose_name=_('Note'))

    company = models.ForeignKey('company.Company', on_delete=models.CASCADE, null=True, related_name='customers')

    history = HistoricalRecords()

    class Meta:
        verbose_name = _('Customer')
        verbose_name_plural = _('Customers')

    def __str__(self):
        return '%s %s - %s - %s' % (self.first_name, self.last_name, self.email, self.phone)


class Address(LastModMixin):
    """Customer Address Model"""
    customer = models.ForeignKey(
        Customer, on_delete=models.SET_NULL,
        null=True, related_name='addresses',
        verbose_name=_('Customer')
    )
    address = models.CharField(max_length=100, verbose_name=_('Address'))
    apartment = models.SmallIntegerField(verbose_name=_('Apartment'))
    entrance = models.SmallIntegerField(verbose_name=_('Entrance'))
    floor = models.SmallIntegerField(verbose_name=_('Floor'))

    history = HistoricalRecords()

    class Meta:
        verbose_name = _('Address')
        verbose_name_plural = _('Address')

    def __str__(self):
        return '%s - %s - %s - %s' % (self.address, self.apartment, self.entrance, self.floor)
