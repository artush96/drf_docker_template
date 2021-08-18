import datetime

from django.db.models import Sum, Q, Count

from apps.choices.enums import CashTypeEnum, OrderStatusEnum
from apps.finances.models import CashBox
from apps.users.models import User
from snippets.utils.datetime import utc_now, get_date_from_request


def get_driver_salary(driver, request):
    dt = get_date_from_request(request)
    date_from = dt['date_from']
    date_to = dt['date_to']
    order_count = driver.orders.filter(
        OrderStatusEnum.COMPLETED,
        start_datetime__date__gte=date_from,
        start_datetime__date__lte=date_to,
    ).count()
    if order_count <= 10:
        salary = order_count * 1000
    else:
        salary = (order_count * 1000) + (order_count * 500)
    return salary


def get_driver_dept(driver, dt):
    if not dt:
        dt = utc_now().date()
    dept = CashBox.objects.filter(to_user=driver, created__date=dt).aggregate(
        total=Sum('amount')
    )
    return dept['total']


def get_finance_detail(request):
    dt_from = get_date_from_request(request).get('dt_from')
    dt_to = get_date_from_request(request).get('dt_to')

    cash = CashBox.objects.filter(
        created__date__gte=dt_from,
        created__date__lte=dt_to
    )

    total_out = Sum(
        'amount', filter=Q(
            created__date=dt_from,
            cash_type=CashTypeEnum.OUT
        )
    )
    total_in = Sum(
        'amount',
        filter=Q(
            created__date=dt_from,
            cash_type=CashTypeEnum.IN
        )
    )
    agg_data = cash.aggregate(
        total_drivers=Count('to_user__id', filter=Q(to_user__is_driver=True)),
        total_out=total_out,
        total_in=total_in,
        total=total_out + total_in
    )

    data = {
        'drivers_count': agg_data['total_drivers'],
        'total_debt': agg_data['total_out'],
        'total_amount': agg_data['total']
    }

    return data


def calculate_cash_register():
    date = utc_now().date()

    amount_in = Sum('amount', filter=Q(cash_type=CashTypeEnum.IN))
    amount_out = Sum('amount', filter=Q(cash_type=CashTypeEnum.OUT))

    cash = CashBox.objects.filter(created__date=date).aggregate(
        total_amount=amount_in + amount_out
    )
    return cash['total_amount']
