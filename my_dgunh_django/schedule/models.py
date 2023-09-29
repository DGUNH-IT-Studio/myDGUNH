from django.db import models
from django.utils import timezone


class Term(models.Model):

    TermNum = models.IntegerField()
    TermStart = models.DateField(blank=True)
    TermEnd = models.DateField(blank=True)

    class Meta:
        ordering = ['TermStart']


class Education_program(models.Model):
    class University_faculty(models.TextChoices):
        IT = 'ФИТиУ', 'Факультет информационных технологий и инженерии'
        LAW = 'ЮФ', 'Юридический факультет'
        ECONOMICS = 'ФЭиУ', 'Факультет экономики и управления'
        FL = 'ФИЯ', 'Факультет иностранных языков'
        AE = 'ФДО', 'Факультет дополнительного образования'

    class Edu_lvl(models.TextChoices):
        BACHELOR = 'Б', 'Бакалавр'
        SPECIALITY = 'С', 'Специалитет'
        MASTER = 'М', 'Магистратура'

    class Edu_form(models.TextChoices):
        FULLTIME = 'О', 'Очная форма'
        CORRESPONDENSE = 'З', 'Заочная форма'
        PARTTIME = 'ОЗ', 'Очно-заочная форма'
        ONLINE = 'ДИСТ', 'Дистанционная форма'
    
    Faculty = models.CharField(
        choices=University_faculty.choices,
    )
    EducationLevel = models.CharField(
        max_length=1,
        choices=Edu_lvl.choices,
    )
    EducationForm = models.CharField(
        max_length=4,
        choices=Edu_form.choices,
        default=Edu_form.FULLTIME,
    )
    EduProgram = models.CharField(
        max_length=256
    )
    
    def __str__(self):
        return self.EduProgram
    
    class Meta:
        ordering = ['Faculty', 'EducationLevel', 'EducationForm', 'EduProgram']


class Group(models.Model):
    EduProgram = models.ForeignKey(
        Education_program, 
        on_delete=models.CASCADE
    )
    Course = models.IntegerField(default=1)
    Stream = models.IntegerField(default=1)
    GroupNum = models.IntegerField(default=1)
    SubGroup = models.IntegerField(blank=True, null=True)


    class Meta:
        ordering = ['EduProgram', 'Course', 'Stream', 'GroupNum']


class Student_schedule(models.Model):
    scheduleID = models.ForeignKey(
        Group, 
        on_delete=models.CASCADE
    )
    Term = models.ForeignKey(
        Term, 
        on_delete=models.CASCADE
    )
    DateStart = models.DateField(default=timezone.now())
    DateEnd = models.DateField(blank=True, default=timezone.now())
    scheduleFile = models.JSONField()

    class Meta:
        ordering = ['Term', 'DateStart']
