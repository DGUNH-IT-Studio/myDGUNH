from django.urls import path
from . import views

urlpatterns = [
    path('form/', views.form),
    path('schedule/', views.show_schedule),
]
