from django.db import models
from django.utils import timezone
from datetime import date


class Terms(models.Model):

    class TermChoices(models.IntegerChoices):
        FIRST = 1
        SECOND = 2

    TermNum = models.IntegerField(
        choices=TermChoices,
    )
    TermStart = models.DateField(default=date.fromisoformat('2023-09-01'))
    TermEnd = models.DateField(default=date.fromisoformat('2023-12-31'))

class EducationProgramms(models.Model):
    class UniversityFaculties(models.TextChoices):
        IT = 'ФИТиУ', 'Факультет информационных технологий и инженерии'
        LAW = 'ЮФ', 'Юридический факультет'
        ECONOMICS = 'ФЭиУ', 'Факультет экономики и управления'
        FL = 'ФИЯ', 'Факультет иностранных языков'
        AE = 'ФДО', 'Факультет дополнительного образования'

    class EduLvls(models.TextChoices):
        BACHELOR = 'Б', 'Бакалавр'
        SPECIALITY = 'С', 'Специалитет'
        MASTER = 'М', 'Магистратура'

    class EduForms(models.TextChoices):
        FULLTIME = 'О', 'Очная форма'
        CORRESPONDENSE = 'З', 'Заочная форма'
        PARTTIME = 'ОЗ', 'Очно-заочная форма'
        ONLINE = 'ДИСТ', 'Дистанционная форма'

    Faculty = models.CharField(
        choices=UniversityFaculties
    )
    EducationLevel = models.CharField(
        max_length=1,
        choices=EduLvls.choices,
    )
    EducationForm = models.CharField(
        max_length=4,
        choices=EduForms.choices,
        default=EduForms.FULLTIME,
    )
    EduProgram = models.CharField(
        max_length=128
    )


class Group(models.Model):
    EduProgram = models.ForeignKey(
        EducationProgramms, 
        on_delete=models.CASCADE
    )
    Course = models.IntegerField(default=1)
    GroupNum = models.IntegerField(default=1)
    Stream = models.IntegerField(default=1)
    SubGroup = models.IntegerField(default=1)
    LabGroup = models.IntegerField(default=1)
    PracticeGroup = models.IntegerField(default=1)


class Schedule(models.Model):
    scheduleID = models.ForeignKey(
        Group, 
        on_delete=models.CASCADE
    )
    Term = models.ForeignKey(
        Terms, 
        on_delete=models.CASCADE
    )
    DateStart = models.DateField(default=timezone.now())
    DateEnd = models.DateField(default=timezone.now())
    scheduleFile = models.JSONField()
