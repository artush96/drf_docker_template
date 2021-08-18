# Generated by Django 3.2.5 on 2021-08-04 13:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import simple_history.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('configs', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='HistoricalBackendEmail',
            fields=[
                ('id', models.BigIntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('created', models.DateTimeField(blank=True, db_index=True, editable=False, verbose_name='Created')),
                ('updated', models.DateTimeField(blank=True, editable=False, verbose_name='Updated')),
                ('use_tls', models.BooleanField(default=False, verbose_name='Use TLS')),
                ('use_ssl', models.BooleanField(default=False, verbose_name='Use SSL')),
                ('host', models.CharField(help_text='smtp.gmail.com', max_length=30, verbose_name='Email HOST')),
                ('port', models.PositiveSmallIntegerField(default=587, help_text='587 for gmail', verbose_name='Email PORT')),
                ('host_user', models.CharField(help_text='me@gmail.com', max_length=50, verbose_name='Host User')),
                ('host_password', models.CharField(help_text='Host USER PASSWORD', max_length=150, verbose_name='Mail PASSWORD')),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'historical backend email',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
    ]
