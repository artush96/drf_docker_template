from django.conf.urls import re_path
from apps.drivers.consumers import GetDriverLocationConsumer


websocket_urlpatterns = [
    re_path(r'location/(?P<company_id>\d+)/(?P<driver_id>\d+)/$', GetDriverLocationConsumer.as_asgi()),
]
