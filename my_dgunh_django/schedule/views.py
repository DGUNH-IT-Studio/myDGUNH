from django.shortcuts import render, get_object_or_404
import json


def form(request):
    data = {}

    return render(request, 'schedule/form.html')


def show_schedule(request):
    data = {}

    return render(request, 'schedule/schedule.html', data)
