# Generated by Django 3.2.5 on 2021-08-04 07:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import simple_history.models


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0005_alter_address_customer'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('orders', '0013_order_canceled'),
    ]

    operations = [
        migrations.CreateModel(
            name='HistoricalOrder',
            fields=[
                ('id', models.BigIntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('created', models.DateTimeField(blank=True, db_index=True, editable=False, verbose_name='Created')),
                ('updated', models.DateTimeField(blank=True, editable=False, verbose_name='Updated')),
                ('payment_type', models.CharField(choices=[('CASH', 'Cash'), ('ONLINE', 'Online')], max_length=6, verbose_name='Payment Type')),
                ('order_status', models.CharField(choices=[('UNASSIGNED', 'Unassigned'), ('ASSIGNED', 'Assigned'), ('COMPLETED', 'Completed'), ('CANCELED', 'Canceled')], default='UNASSIGNED', max_length=10, verbose_name='Order Status')),
                ('canceled', models.BooleanField(verbose_name='Canceled')),
                ('start_datetime', models.DateTimeField(null=True, verbose_name='Start DateTime')),
                ('cancel_datetime', models.DateTimeField(null=True, verbose_name='Cancel DateTime')),
                ('complete_datetime', models.DateTimeField(null=True, verbose_name='Complete DateTime')),
                ('duration', models.FloatField(null=True, verbose_name='Duration')),
                ('first_name', models.CharField(max_length=50, verbose_name='First Name')),
                ('last_name', models.CharField(max_length=50, verbose_name='Last Name')),
                ('phone', models.CharField(max_length=50, verbose_name='Phone')),
                ('price', models.DecimalField(decimal_places=2, max_digits=11, verbose_name='Price')),
                ('order_id', models.PositiveIntegerField(verbose_name='Order ID')),
                ('comment', models.TextField(verbose_name='Comment')),
                ('remind_me', models.BooleanField(default=False, verbose_name='Remind me')),
                ('remind_me_minutes', models.PositiveSmallIntegerField(blank=True, verbose_name='Remind me before - minute')),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('address', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='customers.address', verbose_name='Address')),
                ('customer', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='customers.customer', verbose_name='Customer')),
                ('driver', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to=settings.AUTH_USER_MODEL, verbose_name='Driver')),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'historical Order',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
    ]
