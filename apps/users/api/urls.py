from django.urls import path

from apps.users.api.views import UserListView

urlpatterns = [
    path('list/', UserListView.as_view())
]
