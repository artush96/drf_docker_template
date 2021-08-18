from django.urls import path

from apps.drivers.api.views import (
    DriverCreateView, DriversListView, DriverDetailView,
    DriverOrdersView, DriverActivityView, DriverRatingsView, CreateDriverRatingView, ProfileView
)


urlpatterns = [
    path('<int:company_id>/<int:id>/', ProfileView.as_view(), name='driver_profile'),
    path('<int:company_id>/create/', DriverCreateView.as_view(), name='driver_create'),
    path('<int:company_id>/list/', DriversListView.as_view(), name='driver_list'),
    path('<int:id>/', DriverDetailView.as_view(), name='driver_detail'),
    path('<int:id>/orders/', DriverOrdersView.as_view(), name='driver_orders'),
    path('<int:id>/activities/', DriverActivityView.as_view(), name='driver_activity'),
    path('ratings/create/', CreateDriverRatingView.as_view(), name='create_driver_ratings'),
    path('<int:id>/ratings/', DriverRatingsView.as_view(), name='driver_ratings'),
]
