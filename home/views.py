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

    status_account = ''
    user_name= request.user.username
    user_email=request.user.email
    user_first_name = request.user.first_name
    user_last_name= request.user.last_name

    if not user_email is '':
        if not user_last_name is '':
            if not user_first_name is '':
                status_account = 'Пользовательский'
            else:
                status_account = 'Неполный'
        else:
            status_account = 'Неполный'
    else:
        status_account = 'Ограниченный'


    if user_first_name is '':
        user_first_name = '*Отсутствует*'

    if user_last_name is '':
        user_last_name = '*Отсутствует*'

    #date_reg = request.user.date_joined_0
    #time_reg = request.user.date_joined_1



    data = {
        'email_None': email_None,
        'user_name':user_name,
        'user_email':user_email,
        'user_first_name': user_first_name,
        'user_last_name': user_last_name,
        'status_account': status_account,
        #'date_reg': date_reg,
        #'time_reg': time_reg,
    }
    return render(request, 'registration/profile.html', data)