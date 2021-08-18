from django.contrib.auth.models import Permission, GroupManager, Group
from django.db import models
from django.utils.translation import gettext_lazy as _
from simple_history.models import HistoricalRecords

from snippets.models.abstracts import LastModMixin


class Roles(Group, LastModMixin):
    """Roles Management"""
    company = models.ForeignKey('company.Company', on_delete=models.CASCADE, related_name='roles')

    objects = GroupManager()

    history = HistoricalRecords()

    class Meta:
        verbose_name = _('role')
        verbose_name_plural = _('roles')

    def __str__(self):
        return self.name

    def natural_key(self):
        return self.name
