# Generated by Django 4.0.3 on 2022-05-31 07:31

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('computerApp', '0014_alter_machine_maintenancedate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='machine',
            name='maintenanceDate',
            field=models.DateField(default=datetime.datetime(2022, 5, 31, 7, 31, 34, 425658, tzinfo=utc)),
        ),
    ]
