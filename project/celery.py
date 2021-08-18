import os

from celery import Celery
from celery.schedules import crontab


# Set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')

app = Celery('taskroad_pro')

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django apps.
app.autodiscover_tasks()

app.conf.beat_schedule = {
    # "mul-function": {
    #     "task": "apps.users.tasks.mul",
    #     "schedule": crontab(minute="*/1"),
    # },
    "create-cash-register": {
        "task": "apps.finances.tasks.create_cash_register",
        "schedule": crontab(minute=0, hour='22'),
    },
}
