from django.shortcuts import render, redirect
from django.core.mail import send_mail
from .forms import ContactForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

def home_page(request):
    email_None = ''
    if request.user.is_authenticated:
        if request.user.email == '':
            email_None = 'Ограничено'
    data = {
        'email_None': email_None,
    }
    return render(request, 'home/home_page.html', data)



def test(request):
    email_None = ''
    if request.user.is_authenticated:
        if request.user.email == '':
            email_None = 'Ограничено'

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            send_mail(form.cleaned_data['subject'], form.cleaned_data['content'],'stereotip.228@gmail.com', ['grinwich1211@mail.ru'])
            return redirect('./')
    else:
        form = ContactForm()
    data={
        'form':form,
        'email_None':email_None,
    }
    return render(request, 'home/test.html', data)

def profile(request):
    email_None = ''
    if request.user.is_authenticated:
        if request.user.email == '':
            email_None = 'Ограничено'
    data = {
        'email_None': email_None,
    }
    return render(request, 'registration/profile.html', data)