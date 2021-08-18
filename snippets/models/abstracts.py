from django.db import models
from django.utils.translation import gettext_lazy as _


class CreatedMixin(models.Model):
    """Base model for all models with created fields"""
    created = models.DateTimeField(_('Created'), auto_now_add=True, db_index=True)

    class Meta:
        abstract = True


class LastModMixin(CreatedMixin):
    """Base model for all models with created / updated fields"""
    updated = models.DateTimeField(_('Updated'), auto_now=True)

    class Meta:
        abstract = True
