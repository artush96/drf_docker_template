# Generated by Django 3.2.5 on 2021-08-05 06:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0017_historicalorder_ip_address'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='historicalorder',
            name='ip_address',
        ),
    ]
