# Generated by Django 4.2.3 on 2023-10-15 15:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schedule', '0004_alter_teacher_schedule_view_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacher',
            name='schedule_view_name',
            field=models.CharField(blank=True, max_length=64, null=True),
        ),
    ]
