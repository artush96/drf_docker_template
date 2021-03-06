# Generated by Django 3.2.5 on 2021-08-04 14:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('settings', '0005_historicalgeneralsettings_historicalnotification_historicalterms'),
    ]

    operations = [
        migrations.AddField(
            model_name='historicalgeneralsettings',
            name='ip_address',
            field=models.GenericIPAddressField(default='127.0.0.1', verbose_name='IP address'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='historicalnotification',
            name='ip_address',
            field=models.GenericIPAddressField(default='127.0.0.1', verbose_name='IP address'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='historicalterms',
            name='ip_address',
            field=models.GenericIPAddressField(default='127.0.0.1', verbose_name='IP address'),
            preserve_default=False,
        ),
    ]
