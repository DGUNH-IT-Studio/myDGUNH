from django.shortcuts import render, get_object_or_404
from django.forms import forms
import json


class schedule_choose_form(forms.Form):
    # Форма для выбора расписания
    pass


def index(request):
    data = {}

    return render(request, 'schedule/index.html')


def form(request):
    data = {}

    return render(request, 'schedule/form.html')


def show_schedule(request):
    data = {}

    return render(request, 'schedule/schedule.html', data)
