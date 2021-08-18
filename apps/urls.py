from django.urls import path, include, re_path

from rest_framework import permissions
from rest_framework.documentation import include_docs_urls
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from project import settings

schema_view = get_schema_view(
    openapi.Info(
<<<<<<< HEAD
        title="Django Rest Freamwork API",
        default_version='v1',
=======
        title="ABM Logistics API",
        default_version='v1.0',
>>>>>>> 432334e47cc34b2c64ed06bb81847615c877fc46
        description="Docs",
        # terms_of_service="https://www.google.com/policies/terms/",
        # contact=openapi.Contact(email="contact@snippets.local"),
        # license=openapi.License(name="BSD License"),
    ),
    # url='https://example.com/',
    public=True,
    permission_classes=(permissions.AllowAny,),
)


urlpatterns = [
    # auth urls
    path('auth/', include('apps.auth.urls')),
    # apps urls
    path('users/', include('apps.users.api.urls')),
    path('choices/', include('apps.choices.api.urls')),
    path('settings/', include('apps.settings.api.urls')),
    path('finances/', include('apps.finances.api.urls')),
    path('dashboard/', include('apps.dashboard.api.urls')),
]

if settings.DEBUG:
    urlpatterns += [
        # Doc Urls
        re_path(r'swagger(?P<format>\.json|\.yaml)/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
        path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
        path('docs/', include_docs_urls(title='ABM Logistics API')),
        path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    ]
