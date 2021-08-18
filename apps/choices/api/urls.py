from django.urls import path

from apps.choices.api.views import CarBrandListView, \
    CarModelListView, EnumView, EnumListView

urlpatterns = [
    # path('order-status/', OrderStatusEnumView.as_view(), name='order_status'),
    # path('payment-type/', PaymentTypeEnumView.as_view(), name='payment_type'),
    # path('devices/', DeviceEnumView.as_view(), name='devices'),
    path('car-brands/', CarBrandListView.as_view(), name='car_brands'),
    path('car-brand/<int:id>/models/', CarModelListView.as_view(), name='car_models'),
    path('<str:enum>/', EnumView.as_view(), name='enums'),
    path('', EnumListView.as_view(), name='enums_list'),
]
