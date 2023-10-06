from django.db import models
from django.contrib.auth.models import User
from .static.json.default_professor_schedule import DEFAULT_SCHEDULE


class Department(models.Model):
    DepartmentCode = models.AutoField(primary_key=True)
    DepartmentName = models.CharField(max_length=256)

    def __str__(self):
        return self.DepartmentName


class Professor(models.Model):
    # user = models.OneToOneField(User, on_delete=models.CASCADE)
    Professor_Department = models.ForeignKey(Department, blank=True, null=True)
    FirstName = models.CharField(max_length=64)
    SecondName = models.CharField(max_length=64)
    LastName = models.CharField(max_length=64)
    ScheduleViewName = models.CharField(max_length=64, blank=True, null=True)

    # Here are subjects that professtor is presenting
    Subjects = models.JSONField(blank=True)
    Schedule = models.JSONField(blank=True)

    class Meta:
        unique_together = ('FirstName', 'SecondName', 'LastName', 'Subjects')
