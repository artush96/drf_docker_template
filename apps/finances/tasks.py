from celery import shared_task

from snippets.utils.datetime import utc_now

from apps.finances.api.services import calculate_cash_register
from apps.finances.models import CashRegister


@shared_task
def create_cash_register():
    CashRegister.objects.create(
        chash=calculate_cash_register(),
        date=utc_now()
    )

