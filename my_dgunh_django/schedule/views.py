from django.shortcuts import render, get_object_or_404
from .models import Schedules
import json


def index(request):
    # schedule = get_object_or_404(Schedules, )
    # schedule = ...
    # Необходимо получить расписание по данным пользователя
    # то есть просматриваемое им расписание
    # вытащить Schedules.id и по нему достать Schedules.Schedule
    return render(request, 'schedule/index.html')
