# Generated by Django 3.2.5 on 2021-08-04 14:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0016_auto_20210804_1758'),
    ]

    operations = [
        migrations.AddField(
            model_name='historicalorder',
            name='ip_address',
            field=models.GenericIPAddressField(default='127.0.0.1', verbose_name='IP address'),
            preserve_default=False,
        ),
    ]
