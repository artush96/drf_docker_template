from django.db.models import Sum
from rest_framework import serializers

from apps.choices.enums import OrderStatusEnum
from apps.users.models import User


class DashboardSerializer(serializers.Serializer):
    pending_tasks = serializers.IntegerField()
    ongoing_tasks = serializers.IntegerField()
    finished_tasks = serializers.IntegerField()
    canceled_tasks = serializers.IntegerField()
    delayed_tasks = serializers.IntegerField()
    total_agents = serializers.IntegerField()
    dispatchers = serializers.IntegerField()
    customers = serializers.IntegerField()
    total_dept = serializers.IntegerField()
    avg_delivery_duration = serializers.IntegerField()


class TopDriversSerializer(serializers.ModelSerializer):
    order_count = serializers.IntegerField()
    delay_duration = serializers.IntegerField()
    delayed_order = serializers.SerializerMethodField('get_delayed_order')

    class Meta:
        model = User
        fields = (
            'id', 'image', 'full_name', 'phone',
            'order_count', 'delay_duration', 'delayed_order'
        )

    @staticmethod
    def get_delayed_order(obj):
        return obj.orders.filter(order_status=OrderStatusEnum.COMPLETED)\
            .aggregate(delayed_order=Sum('duration'))['delayed_order']
