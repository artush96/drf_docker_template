from django.db import models
from django.utils.translation import ugettext_lazy as _


class CashTypeEnum(models.TextChoices):
    IN = 'IN', _('IN')
    OUT = 'OUT', _('OUT')


class DeviceEnum(models.TextChoices):
    ANDROID = 'ANDROID', _('Android')
    IOS = 'IOS', _('iOS')


class PaymentTypeEnum(models.TextChoices):
    CASH = 'CASH', _('Cash')
    ONLINE = 'ONLINE', _('Online')


class OrderStatusEnum(models.TextChoices):
    UNASSIGNED = 'UNASSIGNED', _('Unassigned')
    ASSIGNED = 'ASSIGNED', _('Assigned')
    COMPLETED = 'COMPLETED', _('Completed')
    CANCELED = 'CANCELED', _('Canceled')


class OrderDispatcherActivityTypeEnum(models.TextChoices):
    CREATED_BY = 'CREATED_BY', _('Created By')
    CHANGED_BY = 'CHANGED_BY', _('Changed By')


class OrderDriverActivityTypeEnum(models.TextChoices):
    ASSIGNED = 'ASSIGNED', _('Assigned')
    REPLACED = 'REPLACED', _('Replaced')


class CurrencyEnum(models.TextChoices):
    AMD = 'AMD', _('AMD')
    USD = 'USD', _('USD')
