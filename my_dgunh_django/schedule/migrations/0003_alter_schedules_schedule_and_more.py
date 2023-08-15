# Generated by Django 4.2.3 on 2023-08-14 13:33

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schedule', '0002_schedules_eduprogram'),
    ]

    operations = [
        migrations.AlterField(
            model_name='schedules',
            name='Schedule',
            field=models.JSONField(default={}),
        ),
        migrations.AlterField(
            model_name='uniqueschedules',
            name='ChangingDateEnd',
            field=models.DateField(default=datetime.date(2023, 8, 14)),
        ),
        migrations.AlterField(
            model_name='uniqueschedules',
            name='ChangingDateStart',
            field=models.DateField(default=datetime.date(2023, 8, 14)),
        ),
    ]