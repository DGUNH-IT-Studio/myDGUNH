from django.contrib import admin
from .models import *


admin.register(Terms)


@admin.register(Schedules)
class SchedulesAdmin(admin.ModelAdmin):
    ordering = [
        'TermNum', 'EducationLevel', 'EducationForm',
        'Course', 'Stream', 'Group', 'SubGroup',
        'PracticeGroup', 'LabGroup'
    ]

@admin.register(UniqueSchedules)
class UniqueSchedulesAdmin(admin.ModelAdmin):
    ordering = [
        'Schedule_id', 'ChangingDateStart'
    ]
