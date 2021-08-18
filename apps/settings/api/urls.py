from django.urls import path

from apps.settings.api.views import GeneralSettingsDetailView, GeneralSettingsUpdateView, TermsDetailView, \
    TermsUpdateView, NotificationUpdateView, NotificationDetailView

urlpatterns = [
    path('<int:company_id>/general/', GeneralSettingsDetailView.as_view(), name='general_settings_detail'),
    path('<int:company_id>/general/update/', GeneralSettingsUpdateView.as_view(), name='general_settings_update'),
    path('<int:company_id>/terms/', TermsDetailView.as_view(), name='terms_detail'),
    path('<int:company_id>/terms/update/', TermsUpdateView.as_view(), name='terms_update'),
    path('<int:company_id>/notifications/', NotificationDetailView.as_view(), name='notifications_detail'),
    path('<int:company_id>/notifications/update/', NotificationUpdateView.as_view(), name='notifications_update'),
]
