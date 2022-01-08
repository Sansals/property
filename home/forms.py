from django.forms import ModelForm, TextInput, Textarea
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

class ContactForm(forms.Form):
    subject = forms.CharField(label='Email', widget=forms.TextInput(attrs={'class': 'form-control'}))
    content = forms.CharField(label='Текст', widget=forms.Textarea(attrs={'class': 'form-control', 'rows':5}))

class auth_form(forms.Form):
    auth_code = forms.CharField(label='Код подтверждения', widget=forms.TextInput())