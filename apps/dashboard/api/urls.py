from django.urls import path

from apps.dashboard.api.views import DashboardView, TopDriversView

urlpatterns = [
    path('', DashboardView.as_view(), name='dashboard'),
    path('<int:company_id>/top-drivers/', TopDriversView.as_view(), name='top_drivers'),
]
