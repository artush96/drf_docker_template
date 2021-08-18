from django.urls import path

from apps.dispatchers.api.views import (
    DispatcherCreateView, DispatcherListView,
    DispatcherDetailView, DispatcherActivityView,
)

urlpatterns = [
    path('<int:company_id>/create/', DispatcherCreateView.as_view(), name='dispatcher_create'),
    path('<int:company_id>/list/', DispatcherListView.as_view(), name='dispatcher_list'),
    path('<int:id>/', DispatcherDetailView.as_view(), name='dispatcher_detail'),
    path('<int:id>/activities/', DispatcherActivityView.as_view(), name='dispatcher_activities'),
]
