# Generated by Django 3.2.5 on 2021-08-12 07:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0001_initial'),
        ('customers', '0008_auto_20210805_1050'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='company',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='customers', to='company.company'),
        ),
        migrations.AddField(
            model_name='historicalcustomer',
            name='company',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='company.company'),
        ),
    ]
