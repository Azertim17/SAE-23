# Generated by Django 4.0.3 on 2022-05-31 07:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('computerApp', '0011_alter_machine_maintenancedate'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='machine',
            name='maintenanceDate',
        ),
    ]
