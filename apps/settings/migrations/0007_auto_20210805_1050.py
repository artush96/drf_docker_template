# Generated by Django 3.2.5 on 2021-08-05 06:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('settings', '0006_auto_20210804_1833'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='historicalgeneralsettings',
            name='ip_address',
        ),
        migrations.RemoveField(
            model_name='historicalnotification',
            name='ip_address',
        ),
        migrations.RemoveField(
            model_name='historicalterms',
            name='ip_address',
        ),
    ]
