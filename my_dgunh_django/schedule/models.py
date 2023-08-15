from django.db import models
from django.utils import timezone
from datetime import date


class Terms(models.Model):
    TermNum = models.IntegerField(primary_key=True)
    TermStart = models.DateField(default=date.fromisoformat('2023-09-01'))
    TermEnd = models.DateField(default=date.fromisoformat('2023-12-31'))


class Schedules(models.Model):

    class EduLvls(models.TextChoices):
        COLLEGE = 'К', 'Колледж'
        BACHELOR = 'Б', 'Бакалавр'
        SPECIALITY = 'С', 'Специалитет'
        MASTER = 'М', 'Магистратура'

    class EduForms(models.TextChoices):
        FULLTIME = 'О', 'Очная форма'
        CORRESPONDENSE = 'З', 'Заочная форма'
        PARTTIME = 'ОЗ', 'Очно-заочная форма'
        ONLINE = 'ДИСТ', 'Дистанционная форма'


    EducationLevel = models.CharField(
        max_length=1,
        choices=EduLvls.choices,
    )
    EducationForm = models.CharField(
        max_length=4,
        choices=EduForms.choices,
        default=EduForms.FULLTIME,
    )
    EduProgram = models.CharField(max_length=256, default='None')
    Course = models.IntegerField(default=1)
    Group = models.IntegerField(default=1)
    Stream = models.IntegerField(default=1)
    SubGroup = models.IntegerField(default=1)
    LabGroup = models.IntegerField(default=1)
    PracticeGroup = models.IntegerField(default=1)
    TermNum = models.ForeignKey(Terms, on_delete=models.CASCADE)
    Schedule = models.JSONField(default=dict())

class UniqueSchedules(models.Model):
    Schedule_id = models.ForeignKey(
        Schedules,
        on_delete=models.CASCADE
    )
    ChangingDateStart = models.DateField(default=timezone.now())
    ChangingDateEnd = models.DateField(default=timezone.now())
    Schedule = models.JSONField(default=dict())
