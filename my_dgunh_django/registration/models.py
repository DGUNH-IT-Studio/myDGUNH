from django.db import models
from django.contrib.auth.models import User


class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    second_name = models.CharField(max_length=128)
    schedule = models.JSONField(blank=True, null=True)
