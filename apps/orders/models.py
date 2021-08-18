from django.db import models
from django.utils.translation import gettext_lazy as _

from simple_history.models import HistoricalRecords

from apps.choices.enums import PaymentTypeEnum, OrderStatusEnum, OrderDispatcherActivityTypeEnum, \
    OrderDriverActivityTypeEnum
from snippets.models.abstracts import LastModMixin, CreatedMixin
from snippets.models.mixins import CTMixin


class Order(LastModMixin, CTMixin):
    """Order Model"""
    company = models.ForeignKey('company.Company', on_delete=models.CASCADE, related_name='orders')
    payment_type = models.CharField(_('Payment Type'), max_length=6, choices=PaymentTypeEnum.choices)
    order_status = models.CharField(
        _('Order Status'), max_length=10,
        choices=OrderStatusEnum.choices,
        default=OrderStatusEnum.UNASSIGNED
    )
    customer = models.ForeignKey(
        'customers.Customer', on_delete=models.SET_NULL,
        related_name='orders', null=True,
        verbose_name=_('Customer')
    )
    driver = models.ForeignKey(
        'users.User', on_delete=models.SET_NULL,
        related_name='orders', null=True,
        verbose_name=_('Driver')
    )
    canceled = models.BooleanField(null=True, verbose_name=_('Canceled'))

    start_datetime = models.DateTimeField(null=True, verbose_name=_('Start DateTime'))
    cancel_datetime = models.DateTimeField(null=True, verbose_name=_('Cancel DateTime'))
    complete_datetime = models.DateTimeField(null=True, verbose_name=_('Complete DateTime'))
    duration = models.FloatField(null=True, verbose_name=_('Duration'))

    first_name = models.CharField(max_length=50, verbose_name=_('First Name'))
    last_name = models.CharField(max_length=50, verbose_name=_('Last Name'))
    phone = models.CharField(max_length=50, verbose_name=_('Phone'))
    price = models.DecimalField(max_digits=11, decimal_places=2, verbose_name=_('Price'))
    order_id = models.PositiveIntegerField(verbose_name=_('Order ID'))
    comment = models.TextField(null=True, verbose_name=_('Comment'))
    address = models.ForeignKey('customers.Address', on_delete=models.SET_NULL, null=True, verbose_name=_('Address'))
    remind_me = models.BooleanField(_('Remind me'), default=False)
    remind_me_minutes = models.PositiveSmallIntegerField(blank=True, verbose_name=_('Remind me before - minute'))

    history = HistoricalRecords()

    class Meta:
        verbose_name = _('Order')
        verbose_name_plural = _('Orders')

    def __str__(self):
        return '%s - %s' % (self.price, self.address)


class OrderActivity(CreatedMixin):
    """Order Status Activity model"""
    order = models.ForeignKey(
        Order, on_delete=models.SET_NULL,
        null=True, related_name='status_activity',
        verbose_name=_('Order')
    )
    order_status = models.CharField(_('Order Status'), max_length=10, choices=OrderStatusEnum.choices)

    class Meta:
        verbose_name = _('Order Activity')
        verbose_name_plural = _('Order Activities')

    def __str__(self):
        return '%s - %s' % (self.order, self.order_status)


class OrderDispatcherActivity(CreatedMixin):
    """Order dispatches (created by, changed by, ...) model"""
    dispatcher = models.ForeignKey(
        'users.User', on_delete=models.SET_NULL,
        related_name='dispatcher_activity', null=True,
        verbose_name=_('Dispatcher')
    )
    order = models.ForeignKey(
        Order, on_delete=models.SET_NULL,
        null=True, related_name='dispatchers',
        verbose_name=_('Order')
    )
    order_status = models.CharField(_('Order Status'), max_length=10, choices=OrderStatusEnum.choices)
    activity_type = models.CharField(
        max_length=15,
        choices=OrderDispatcherActivityTypeEnum.choices,
        verbose_name=_('Activity Type')
    )

    class Meta:
        verbose_name = _('Order Dispatcher Activity')
        verbose_name_plural = _('Order Dispatcher Activities')

    def __str__(self):
        return '%s - %s' % (self.dispatcher, self.activity_type)


class OrderDriverActivity(CreatedMixin):
    """Order drivers activity model"""
    driver = models.ForeignKey(
        'users.User', on_delete=models.SET_NULL,
        related_name='diver_activity', null=True,
        verbose_name=_('Driver')
    )
    dispatcher = models.ForeignKey(
        'users.User', on_delete=models.SET_NULL,
        null=True, verbose_name=_('Dispatcher')
    )
    order = models.ForeignKey(
        Order, on_delete=models.SET_NULL,
        null=True, related_name='drivers',
        verbose_name=_('Order')
    )
    activity_type = models.CharField(
        max_length=15,
        choices=OrderDriverActivityTypeEnum.choices,
        verbose_name=_('Activity Type')
    )
    replaced_from = models.ForeignKey(
        'users.User', on_delete=models.SET_NULL,
        null=True, related_name='replaced_from',
        verbose_name=_('Replaced From')
    )
    replaced_to = models.ForeignKey(
        'users.User', on_delete=models.SET_NULL,
        null=True, related_name='replaced_to',
        verbose_name=_('Replaced To')
    )

    class Meta:
        verbose_name = _('Order Driver Activity')
        verbose_name_plural = _('Order Driver Activities')

    def __str__(self):
        return '%s - %s' % (self.driver, self.activity_type)
