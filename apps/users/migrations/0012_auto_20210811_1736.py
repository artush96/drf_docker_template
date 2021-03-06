# Generated by Django 3.2.5 on 2021-08-11 13:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0001_initial'),
        ('users', '0011_remove_historicaluser_ip_address'),
    ]

    operations = [
        migrations.AddField(
            model_name='historicaluser',
            name='company',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='company.company'),
        ),
        migrations.AddField(
            model_name='historicaluser',
            name='is_online',
            field=models.BooleanField(default=True, null=True, verbose_name='Online'),
        ),
        migrations.AddField(
            model_name='user',
            name='company',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='employers', to='company.company'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='is_online',
            field=models.BooleanField(default=True, null=True, verbose_name='Online'),
        ),
    ]
