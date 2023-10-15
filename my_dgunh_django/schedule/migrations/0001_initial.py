# Generated by Django 4.2.3 on 2023-10-15 14:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('department_name', models.CharField(max_length=256, unique=True)),
                ('subjects', models.JSONField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='education_profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile', models.CharField(max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name='education_program',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('education_level', models.CharField(choices=[('Б', 'Бакалавр'), ('С', 'Специалитет'), ('М', 'Магистратура')], max_length=1)),
                ('education_form', models.CharField(choices=[('О', 'Очная форма'), ('З', 'Заочная форма'), ('ОЗ', 'Очно-заочная форма'), ('ДИСТ', 'Дистанционная форма')], default='О', max_length=4)),
                ('education_program_name', models.CharField(blank=True, max_length=256, null=True)),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='schedule.education_profile')),
            ],
        ),
        migrations.CreateModel(
            name='teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=64)),
                ('second_name', models.CharField(max_length=64)),
                ('last_name', models.CharField(max_length=64)),
                ('schedule_view_name', models.CharField(blank=True, max_length=64, null=True)),
                ('teacher_department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='schedule.department')),
            ],
        ),
        migrations.CreateModel(
            name='university_group',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course', models.IntegerField(default=1)),
                ('stream', models.IntegerField(default=1)),
                ('group_num', models.IntegerField(default=1)),
                ('subgroup_num', models.IntegerField(blank=True, null=True)),
                ('group_education_program', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='schedule.education_program')),
            ],
        ),
        migrations.CreateModel(
            name='university_faculty',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('faculty_full_name', models.CharField(max_length=128)),
                ('faculty_short_name', models.CharField(blank=True, max_length=32, null=True)),
            ],
            options={
                'unique_together': {('faculty_full_name', 'faculty_short_name')},
            },
        ),
        migrations.CreateModel(
            name='term',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('term_num', models.IntegerField()),
                ('term_start', models.DateField(blank=True)),
                ('term_end', models.DateField(blank=True)),
            ],
            options={
                'unique_together': {('term_num', 'term_start', 'term_end')},
            },
        ),
        migrations.CreateModel(
            name='teacher_schedule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('teacher_schedule', models.JSONField(blank=True)),
                ('last_update', models.DateTimeField(auto_now_add=True)),
                ('teacher_info', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='schedule.teacher')),
            ],
        ),
        migrations.CreateModel(
            name='student_schedule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_start', models.DateField(blank=True)),
                ('date_end', models.DateField(blank=True)),
                ('schedule_object', models.JSONField(blank=True)),
                ('date_add', models.DateTimeField(auto_now=True)),
                ('lastupdate', models.DateTimeField(auto_now_add=True)),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='schedule.university_group')),
                ('term_num', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='schedule.term')),
            ],
        ),
        migrations.AddField(
            model_name='education_profile',
            name='faculty',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='schedule.university_faculty'),
        ),
        migrations.AlterUniqueTogether(
            name='education_profile',
            unique_together={('faculty', 'profile')},
        ),
    ]
