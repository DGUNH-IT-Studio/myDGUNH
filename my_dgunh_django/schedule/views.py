from django.shortcuts import render, get_object_or_404
import json


def show_schedule(request):
    data = {}

    return render(request, 'schedule/index.html')
