import datetime

from django.conf import settings
from django.utils import timezone

import pytz


def local_to_utc(dt):
    if dt is None:
        return None

    tz = pytz.timezone(settings.TIME_ZONE)

    utc_dt = dt - tz.utcoffset(dt)
    if utc_dt.tzinfo is None:
        utc_dt = utc_dt.replace(tzinfo=timezone.utc)
    return utc_dt


def utc_now():
    return timezone.now()


def local_now(date_format=False):
    now = timezone.localtime(timezone.now())

    if date_format:
        return now.strftime('%d.%m.%Y %H:%M:%S')

    return now


def get_date_from_request(request):
    dt_from = request.data.get('dt_from')
    dt_to = request.data.get('dt_to')
    data = {}
    if not dt_from:
        dt_from = utc_now().date()
        data['dt_from'] = dt_from
    if not dt_to:
        dt_to = dt_from
        data['dt_to'] = dt_to

    return data
