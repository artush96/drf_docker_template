from django.conf.urls.i18n import i18n_patterns
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth.models import Group
from django.urls import path, include

from apps.auth.forms import CustomAuthenticationForm
from project import settings


admin.autodiscover()
admin.site.login_form = CustomAuthenticationForm
# admin.site.enable_nav_sidebar = False
admin.site.site_title = 'Django Admin'
admin.site.site_header = 'Django Logistics'


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('api/v1.0/', include('apps.urls')),
]
# urlpatterns += i18n_patterns(
#     path('admin/', admin.site.urls)
# )

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
