import random
from celery import shared_task
from celery.schedules import crontab
from project.celery import app


@app.task
def send_mail():
    return


@app.task
def send_sms():
    return


@shared_task
def mul():
    x, y = 5, 7
    total = x * (y * random.randint(3, 100))
    return total


@shared_task(name="sum_list_numbers")
def xsum(numbers):
    return sum(numbers)




