# Generated by Django 3.2.5 on 2021-08-17 06:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('drivers', '0007_auto_20210805_1050'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='driver',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='car', to=settings.AUTH_USER_MODEL, verbose_name='Driver'),
        ),
        migrations.CreateModel(
            name='Revenue',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Created')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=11, verbose_name='Amount')),
                ('driver', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='revenues', to=settings.AUTH_USER_MODEL, verbose_name='Driver')),
            ],
            options={
                'verbose_name': 'Revenue',
                'verbose_name_plural': 'Revenues',
            },
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Created')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Updated')),
                ('latitude', models.CharField(max_length=50, verbose_name='Latitude')),
                ('longitude', models.CharField(max_length=50, verbose_name='Longitude')),
                ('driver', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Driver')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]