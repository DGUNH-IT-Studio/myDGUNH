from django.shortcuts import render
from django import forms
from django.contrib.auth.forms import AuthenticationForm


class registration(forms.Form):
    first_name = forms.CharField(label='Your first name', required=True, max_length=128)
    second_name = forms.CharField(label='Your second name', required=True, max_length=128)
    last_name = forms.CharField(label='Your last name', required=True, max_length=128)
    email = forms.EmailField(label='Your e-mail', required=True)


def index(request):
    return render(request, 'registration/sign-in.html')
