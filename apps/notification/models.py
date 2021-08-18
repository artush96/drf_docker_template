from django.db import models
from django.utils.translation import gettext_lazy as _

from snippets.models.abstracts import LastModMixin


# class Notification(LastModMixin):
#     """Notification model"""
#     device_token = models.CharField(max_length=50, verbose_name=_('Device Token'))
#     subject = models.BooleanField(default=False, verbose_name=_('Subject'))
#     email = models.BooleanField(default=False, verbose_name=_('Email'))
