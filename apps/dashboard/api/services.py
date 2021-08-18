from django.db.models import Count, Q, Avg, Sum

from apps.choices.enums import OrderStatusEnum
from apps.company.models import Company
from apps.orders.models import Order


def get_dashboard_detail(request):
    date_from = request.data.get('date_from')
    date_to = request.data.get('date_to')

    company_id = request.data.get('company_id')

    query_params = {}
    if date_from:
        query_params['start_datetime__date__gte'] = date_from,
    if date_to:
        query_params['start_datetime__date__lte'] = date_to,

    orders = Order.objects.filter(
        company_id=company_id,
        **query_params
    ).aggregate(
        pending_tasks=Count('id', filter=Q(order_status=OrderStatusEnum.UNASSIGNED)),
        ongoing_tasks=Count('id', filter=Q(order_status=OrderStatusEnum.ASSIGNED)),
        finished_tasks=Count('id', filter=Q(order_status=OrderStatusEnum.COMPLETED)),
        canceled_tasks=Count('id', filter=Q(order_status=OrderStatusEnum.CANCELED)),
        delayed_tasks=Count('id', filter=Q(order_status=OrderStatusEnum.CANCELED)),
        avg_delivery_duration=Avg('duration', filter=Q(order_status=OrderStatusEnum.COMPLETED)),

    )
    company = Company.objects.filter(id=company_id).aggregate(
        total_agents=Count('employers', filter=Q(employers__is_driver=True)),
        dispatchers=Count('employers', filter=Q(employers__is_dispatcher=True)),
        customers=Count('customers'),
        total_dept=Sum('employers__transfers_out__amount', filter=Q(employers__is_driver=True))
    )

    return orders | company

