from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


def validate_only_count_instance(obj, count):
    model = obj.__class__
    if model.objects.count() > 0 and obj.id != model.objects.get().id:
        raise ValidationError(_('Can create %s %s instance.') % (count, model.__name__))
