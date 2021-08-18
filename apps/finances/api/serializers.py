from django.db.models import Sum
from rest_framework import serializers

from apps.choices.enums import PaymentTypeEnum, OrderStatusEnum, CashTypeEnum
from apps.finances.api.services import get_driver_salary, get_driver_dept
from apps.finances.models import DriversDept, DriversRepayment, DriversSalary, CashRegister, CashBox
from apps.orders.models import Order
from apps.users.models import User
from snippets.utils.datetime import utc_now, get_date_from_request


class DriversDeptSerializer(serializers.ModelSerializer):
    class Meta:
        model = DriversDept
        fields = ('id', 'driver', 'dispatcher', 'amount')


class DriversRepaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = DriversRepayment
        fields = ('id', 'driver', 'dispatcher', 'amount')


class DriversSalarySerializer(serializers.ModelSerializer):
    class Meta:
        model = DriversSalary
        fields = ('id', 'driver', 'dispatcher', 'amount')


class CashRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = CashRegister
        fields = ('id', 'date', 'cash')


class OrderSerializer(serializers.ModelSerializer):
    debt = serializers.SerializerMethodField('get_debt')

    class Meta:
        model = Order
        fields = (
            'id', 'payment_type', 'price', 'debt'
        )

    @staticmethod
    def get_debt(obj):
        if obj.payment_type == PaymentTypeEnum.ONLINE:
            return None
        return obj.price


class CashBoxSerializer(serializers.ModelSerializer):

    class Meta:
        model = CashBox
        fields = (
            'id', 'created', 'amount', 'cash_type'
        )


class RepaymentSerializer(serializers.ModelSerializer):
    total_amount = serializers.SerializerMethodField('get_total_amount')

    class Meta:
        model = DriversRepayment
        fields = (
            'id', 'created', 'amount', 'total_amount'
        )

    @staticmethod
    def get_total_amount(obj):
        return obj.driver.transfers_out.aggregate(total_amount=Sum('amount'))['total_amount']


class FinanceListSerializer(serializers.ModelSerializer):
    ongoing_orders = serializers.SerializerMethodField('get_ongoing_orders')
    today_orders = serializers.SerializerMethodField('get_today_orders')
    debt = serializers.SerializerMethodField('get_debt')
    salary = serializers.SerializerMethodField('get_salary')

    class Meta:
        model = User
        fields = (
            'id', 'full_name', 'phone', 'today_orders',
            'ongoing_orders', 'debt', 'salary',
        )

    @staticmethod
    def get_ongoing_orders(obj):
        return obj.orders.filter(order_status=OrderStatusEnum.ASSIGNED).count()

    @staticmethod
    def get_today_orders(obj):
        return obj.orders.filter(start_datetime__date=utc_now().date()).count()

    def get_debt(self, obj):
        request = self.context.get('request')
        dt = get_date_from_request(request).get('dt_from')
        return get_driver_dept(obj, dt)

    def get_salary(self, obj):
        return get_driver_salary(obj, self.context.get('request'))


class FinanceSerializer(serializers.Serializer):
    drivers_count = serializers.IntegerField()
    total_debt = serializers.DecimalField(max_digits=11, decimal_places=2)
    total_amount = serializers.DecimalField(max_digits=11, decimal_places=2)


class FinanceDriverDetailSerializer(serializers.Serializer):
    orders_total = serializers.SerializerMethodField('get_order_total')
    dept_total = serializers.SerializerMethodField('get_dept_total')
    repayment_total = serializers.SerializerMethodField('get_repayment_total')
    orders_cash_total = serializers.SerializerMethodField('get_order_total')
    orders_online_total = serializers.SerializerMethodField('get_orders_online_total')
    orders = serializers.SerializerMethodField('get_orders')
    cash_debt = serializers.SerializerMethodField('get_cash_debt')
    cash_repayment = serializers.SerializerMethodField('get_cash_repayment')

    def get_dt(self):
        request = self.context.get('request')
        dt = get_date_from_request(request).get('dt_from')
        return dt

    def get_orders(self, obj):
        return obj.orders.filter(
            start_datetime__date=self.get_dt()
        )

    def get_order_total(self, obj):
        return obj.orders.filter(
            start_datetime__date=self.get_dt(),
            payment_type=PaymentTypeEnum.CASH
        ).aggregate(total=Sum('price'))['total']

    def get_orders_online_total(self, obj):
        return obj.orders.filter(
            start_datetime__date=self.get_dt(),
            payment_type=PaymentTypeEnum.ONLINE
        ).aggregate(total=Sum('price'))['total']

    def get_dept_total(self, obj):
        return obj.transfers_in.filter(
            created=self.get_dt(),
            cash_type=CashTypeEnum.OUT
        ).aggregate(
            total_amount=Sum('amount')
        )['total_amount']

    def get_repayment_total(self, obj):
        return obj.transfers_out.filter(
            created=self.get_dt(),
            cash_type=CashTypeEnum.IN
        ).aggregate(
            total_amount=Sum('amount')
        )['total_amount']

    def get_cash_debt(self, obj):
        queryset = CashBox.objects.filter(
            created=self.get_dt(),
            cash_type=CashTypeEnum.OUT,
            to_user=obj
        )
        return CashBoxSerializer(queryset, many=True).data

    def get_cash_repayment(self, obj):
        queryset = CashBox.objects.filter(
            created=self.get_dt(),
            cash_type=CashTypeEnum.IN,
            from_user=obj
        )
        return CashBoxSerializer(queryset, many=True).data
