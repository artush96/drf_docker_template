from django.db import models
from django.utils.translation import gettext_lazy as _
from snippets.models.abstracts import LastModMixin


class Company(LastModMixin):
    name = models.CharField(max_length=50, verbose_name=_('Company'))

    class Meta:
        verbose_name = 'Company'
        verbose_name_plural = 'Companies'
