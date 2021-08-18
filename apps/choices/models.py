from django.db import models
from django.utils.translation import gettext_lazy as _


class CarBrand(models.Model):
    name = models.CharField(max_length=50, verbose_name=_('Brand'))


class CarModel(models.Model):
    name = models.CharField(max_length=50, verbose_name=_('Model'))
    brand = models.ForeignKey(
        CarBrand, on_delete=models.CASCADE,
        blank=True, verbose_name=_('Brand')
    )
