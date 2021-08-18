from django.urls import path

from rest_framework_simplejwt.views import TokenRefreshView
from apps.auth.views import (ChangePasswordView, PasswordResetEmailView,
                             PasswordTokenCheckView, SetPasswordView, TokenGenerateView)

urlpatterns = [
    # token get and refresh
    path('token/', TokenGenerateView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    # profile password change
    path('password/change/', ChangePasswordView.as_view(), name='password_change'),
    # password reset
    path('password/reset/', PasswordResetEmailView.as_view(), name='password_reset_email'),
    path('password/reset/<uidb64>/<token>/', PasswordTokenCheckView.as_view(), name='password_reset_confirm'),
    path('password/reset/complete/', SetPasswordView.as_view(), name='password_reset_complete'),

]
