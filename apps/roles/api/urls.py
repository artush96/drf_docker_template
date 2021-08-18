from django.urls import path

from apps.roles.api.views import GroupView


urlpatterns = [
    path('<int:company_id>/', GroupView.as_view(), name='roles'),
    path('<int:company_id>/<int:id>/', GroupView.as_view(), name='roles'),
]
