# Generated by Django 4.0.3 on 2022-05-28 11:07

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('computerApp', '0007_alter_machine_maintenancedate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='machine',
            name='maintenanceDate',
            field=models.DateField(default=datetime.datetime(2022, 5, 28, 11, 7, 18, 284619)),
        ),
    ]
