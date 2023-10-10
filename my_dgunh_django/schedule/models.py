from django.db import models
from django.utils import timezone


DEFAULT_PROFESSOR_SCHEDULE = [
    {
        "Monday": [],
        "Tuesday": [],
        "Wednsday": [],
        "Thursday": [],
        "Friday": [],
        "Saturday": []
    },
    {
        "Monday": [],
        "Tuesday": [],
        "Wednsday": [],
        "Thursday": [],
        "Friday": [],
        "Saturday": []
    }
]


class Term(models.Model):
    TermNum = models.IntegerField()
    TermStart = models.DateField(blank=True)
    TermEnd = models.DateField(blank=True)

    class Meta:
        ordering = ['TermStart']
        unique_together = ('TermNum', 'TermStart', 'TermEnd')


class University_Faculty(models.Model):
    faculty_full_name = models.CharField(max_length=128, blank=False)
    faculty_short_name = models.CharField(max_length=32, blank=True, null=True)

    def __str__(self):
        return self.faculty_full_name

    class Meta:
        unique_together = ['faculty_full_name', 'faculty_short_name']


class Education_program(models.Model):
    class Edu_lvl(models.TextChoices):
        BACHELOR = 'Б', 'Бакалавр'
        SPECIALITY = 'С', 'Специалитет'
        MASTER = 'М', 'Магистратура'

    class Edu_form(models.TextChoices):
        FULLTIME = 'О', 'Очная форма'
        CORRESPONDENSE = 'З', 'Заочная форма'
        PARTTIME = 'ОЗ', 'Очно-заочная форма'
        ONLINE = 'ДИСТ', 'Дистанционная форма'

    Faculty = models.ForeignKey(University_Faculty, on_delete=models.CASCADE)
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
        max_length=256,
        blank=True,
        null=True
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
    Term_num = models.ForeignKey(
        Term,
        on_delete=models.CASCADE
    )
    DateStart = models.DateField(blank=True)
    DateEnd = models.DateField(blank=True)
    scheduleFile = models.JSONField(blank=True)
    lastupdate = models.DateTimeField(auto_now=True)


    class Meta:
        ordering = ['Term_num', 'DateStart']

class Department(models.Model):
    DepartmentCode = models.AutoField(primary_key=True, unique=True)
    DepartmentName = models.CharField(max_length=256, unique=True)
    Subjects = models.JSONField(blank=True)

    def __str__(self):
        return self.DepartmentName
    
    class Meta:
        pass


class Professor(models.Model):
    # user = models.OneToOneField(User, on_delete=models.CASCADE)
    Professor_Department = models.ForeignKey(Department, blank=True, null=True)
    FirstName = models.CharField(max_length=64)
    SecondName = models.CharField(max_length=64)
    LastName = models.CharField(max_length=64)
    ScheduleViewName = models.CharField(max_length=64, blank=True, null=True)


    def __str__(self):
        return str(self.SecondName).capitalize() + ' ' + \
               str(self.FirstName)[0].upper() + '.' + \
               str(self.LastName)[0].upper() + '.'


    class Meta:
        unique_together = ('FirstName', 'SecondName', 'LastName', 'Subjects')

class Professor_schedule(models.Model):
    ProfessorID = models.ForeignKey(Professor, on_delete=models.CASCADE)
    Schedule = models.JSONField(default=DEFAULT_PROFESSOR_SCHEDULE, blank=True)
    last_update = models.DateTimeField(auto_now=True)
