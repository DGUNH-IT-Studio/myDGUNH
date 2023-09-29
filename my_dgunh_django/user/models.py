from django.db import models
# from django.contrib.auth.models import User
# from ..schedule.models import Group
from .static.json.default_professor_schedule import DEFAULT_SCHEDULE


# class Student(models.Model):

#     # class AuthorizationMethod(models.TextChoices):

#     #     DEFAULT = 'Default', 'Default Auth Method'
#     #     SBER_ID = 'Sber', 'Sber ID'
#     #     TINKOFF_ID = 'Tinkoff', 'Tinkoff ID'
#     #     YANDEX_ID = 'Ya', 'Yandex Pass'
#     #     GOOGLE_ID = 'Google', 'Google Mail'
#     #     VK_ID = 'VK', 'VK ID'


#     GroupID = models.ForeignKey(Group, on_delete=models.CASCADE)
#     # AuthMethod = models.CharField(
#     #     default=AuthorizationMethod.DEFAULT, 
#     #     choices=AuthorizationMethod.choices
#     # )
#     # UserName = models.CharField(max_length=32)
#     Email = models.EmailField(unique=True)
#     FirstName = models.CharField(max_length=64)
#     SecondName = models.CharField(max_length=64)
#     LastName = models.CharField(max_length=64)
#     # isHead = models.BooleanField(default=False)
#     ChosenSchedule = models.ForeignKey(Schedule, on_delete=models.CASCADE)


class Department(models.Model):
    DepartmentCode = models.AutoField(primary_key=True)
    DepartmentName = models.CharField(max_length=256)

    def __str__(self):
        return self.DepartmentName


class Professor(models.Model):
    Professor_Department = models.ForeignKey(Department, on_delete=models.CASCADE)
    FirstName = models.CharField(max_length=64)
    SecondName = models.CharField(max_length=64)
    LastName = models.CharField(max_length=64)
    ScheduleViewName = models.CharField(max_length=64, blank=True, null=True)

    # Here are subjects that professtor is presenting
    Subjects = models.JSONField(blank=True)
    Schedule = models.JSONField(blank=True, default=DEFAULT_SCHEDULE)

    class Meta:
        unique_together = ('FirstName', 'SecondName', 'LastName', 'Subjects')


# class Administrator(models.Model):

#     UserName = models.CharField(max_length=32)
#     FirstName = models.CharField(max_length=64)
#     SecondName = models.CharField(max_length=64)
#     LastName = models.CharField(max_length=64)
