from django.db import models
from django.utils.translation import ugettext_lazy as _
from simple_history.models import HistoricalRecords

from apps.choices.enums import CashTypeEnum
from snippets.models.abstracts import CreatedMixin, LastModMixin


class DriversSalary(CreatedMixin):
    """Driver Salary model"""
    driver = models.ForeignKey(
        'users.User', on_delete=models.SET_NULL,
        null=True, related_name='transferred_salaries',
        verbose_name=_('Driver')
    )
    dispatcher = models.ForeignKey(
        'users.User', on_delete=models.SET_NULL,
        null=True, related_name='salary_transfers',
        verbose_name=_('Dispatcher')
    )
    amount = models.DecimalField(max_digits=11, decimal_places=2, verbose_name=_('Amount'))

    history = HistoricalRecords()

    class Meta:
        verbose_name = _('Salary')
        verbose_name_plural = _('Salaries')

    def __str__(self):
        return '%s - %s' % (self.driver, self.amount)


class CashBox(CreatedMixin):
    from_user = models.ForeignKey(
        'users.User', on_delete=models.SET_NULL,
        null=True, related_name='transfers_out',
        verbose_name=_('From')
    )
    to_user = models.ForeignKey(
        'users.User', on_delete=models.SET_NULL,
        null=True, related_name='transfers_in',
        verbose_name=_('To')
    )
    cash_type = models.CharField(max_length=3, choices=CashTypeEnum.choices)
    amount = models.DecimalField(max_digits=11, decimal_places=2, verbose_name=_('Amount'))

    history = HistoricalRecords()

    class Meta:
        verbose_name = _('Cash Box')
        verbose_name_plural = _('Cash Box')

    def __str__(self):
        return '%s - %s' % (self.amount, self.cash_type)

    def clean(self):
        if self.cash_type == CashTypeEnum.OUT:
            self.amount = -self.amount


class DriversDept(CreatedMixin):
    """Driver deposit model"""
    driver = models.ForeignKey(
        'users.User', on_delete=models.SET_NULL,
        null=True, related_name='driver_depts',
        verbose_name=_('Driver')
    )
    dispatcher = models.ForeignKey(
        'users.User', on_delete=models.SET_NULL,
        null=True, related_name='depts',
        verbose_name=_('Dispatcher')
    )
    amount = models.DecimalField(max_digits=11, decimal_places=2, verbose_name=_('Amount'))

    history = HistoricalRecords()

    class Meta:
        verbose_name = _('Dept')
        verbose_name_plural = _('Depts')

    def __str__(self):
        return '%s - %s' % (self.driver, self.amount)


class DriversRepayment(CreatedMixin):
    """Driver repayment model"""
    driver = models.ForeignKey(
        'users.User', on_delete=models.SET_NULL,
        null=True, related_name='driver_repayments',
        verbose_name=_('Driver')
    )
    dispatcher = models.ForeignKey(
        'users.User', on_delete=models.SET_NULL,
        null=True, related_name='repayments',
        verbose_name=_('Dispatcher')
    )
    amount = models.DecimalField(max_digits=11, decimal_places=2, verbose_name=_('Amount'))

    history = HistoricalRecords()

    class Meta:
        verbose_name = _('Repayment')
        verbose_name_plural = _('Repayments')

    def __str__(self):
        return '%s - %s' % (self.driver, self.amount)


class CashRegister(LastModMixin):
    """Cash Register model"""
    company = models.ForeignKey('company.Company', on_delete=models.CASCADE, related_name='cash_register')
    cash = models.DecimalField(max_digits=11, decimal_places=2, verbose_name=_('Cash'))
    date = models.DateField(verbose_name=_('Cash date'))

    history = HistoricalRecords()

    class Meta:
        verbose_name = _('Cash')
        verbose_name_plural = _('Cash')

    def __str__(self):
        return '%s - %s' % (self.date, self.cash)
