from django.urls import path

from apps.orders.api.views import OrderCreateView, OrderListView, OrderDetailView, OrderDetailHistoryView, \
    OrderCancelView

urlpatterns = [
    path('<int:company_id>/create/', OrderCreateView.as_view(), name='order_create'),
    path('<int:company_id>/list/', OrderListView.as_view(), name='order_list'),
    path('<int:company_id>/<int:id>/', OrderDetailView.as_view(), name='order_detail'),
    path('<int:company_id>/<int:id>/cancel/', OrderCancelView.as_view(), name='order_cancel'),
    path('<int:company_id>/<int:id>/history/', OrderDetailHistoryView.as_view(), name='order_detail_history'),
]
