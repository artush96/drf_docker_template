from django.db import models
from django.utils.translation import gettext_lazy as _
from simple_history.models import HistoricalRecords

from snippets.models.abstracts import LastModMixin
from snippets.models.creating_limit import validate_only_count_instance


class BackendEmail(LastModMixin):
    """Email settings for sending mail"""
    use_tls = models.BooleanField(default=False, verbose_name=_('Use TLS'))
    use_ssl = models.BooleanField(default=False, verbose_name=_('Use SSL'))
    host = models.CharField(max_length=30, verbose_name=_('Email HOST'), help_text='smtp.gmail.com')
    port = models.PositiveSmallIntegerField(default=587, verbose_name=_('Email PORT'), help_text='587 for gmail')
    host_user = models.CharField(max_length=50, verbose_name=_('Host User'), help_text='me@gmail.com')
    host_password = models.CharField(max_length=150, verbose_name=_('Mail PASSWORD'), help_text='Host USER PASSWORD')

    history = HistoricalRecords()

    def clean(self):
        validate_only_count_instance(self, 1)
