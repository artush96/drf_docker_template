from django.db import models
from django.utils.translation import gettext_lazy as _
from simple_history.models import HistoricalRecords

from snippets.models.abstracts import LastModMixin, CreatedMixin


class Revenue(CreatedMixin):
    """Driver revenue Model"""
    driver = models.ForeignKey(
        'users.User', on_delete=models.CASCADE, related_name='revenues',
        verbose_name=_('Driver')
    )
    amount = models.DecimalField(max_digits=11, decimal_places=2, verbose_name=_('Amount'))

    class Meta:
        verbose_name = 'Revenue'
        verbose_name_plural = 'Revenues'


class DriverRating(CreatedMixin):
    """Driver rating model"""
    driver = models.ForeignKey(
        'users.User', on_delete=models.SET_NULL,
        related_name='ratings', null=True,
        verbose_name=_('Driver')
    )
    order = models.ForeignKey(
        'orders.Order', on_delete=models.SET_NULL,
        null=True, verbose_name=_('Order')
    )
    comment = models.TextField(max_length=1000, blank=True, verbose_name=_('Comment'))
    rating = models.PositiveSmallIntegerField(verbose_name=_('Rating'))

    history = HistoricalRecords()

    class Meta:
        verbose_name = _('Driver Rating')
        verbose_name_plural = _('Driver Ratings')

    def __str__(self):
        return '%s - %s' % (self.driver, self.rating)


class Car(LastModMixin):
    driver = models.OneToOneField(
        'users.User', on_delete=models.CASCADE,
        related_name='car', verbose_name=_('Driver')
    )
    model = models.ForeignKey(
        'choices.CarModel', on_delete=models.CASCADE,
        verbose_name=_('Driver car')
    )
    plate = models.CharField(max_length=15, verbose_name='Plate')


class AttachedFiles(LastModMixin):
    """Car attached files Model"""
    car = models.ForeignKey(Car, on_delete=models.SET_NULL, null=True, verbose_name='Car', related_name='files')
    file = models.FileField('File', upload_to='car/files/%Y/%m/%d')

    history = HistoricalRecords()

    class Meta:
        verbose_name = _('Attached File')
        verbose_name_plural = _('Attached Files')

    def __str__(self):
        return '%s - %s' % (self.car if self.car else _('Not User'), self.file)


class Location(LastModMixin):
    driver = models.ForeignKey('users.User', on_delete=models.CASCADE, verbose_name=_('Driver'))
    latitude = models.CharField(max_length=50, verbose_name=_('Latitude'))
    longitude = models.CharField(max_length=50, verbose_name=_('Longitude'))
