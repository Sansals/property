from django.shortcuts import render, redirect
from django.core.mail import send_mail
from .forms import ContactForm
from django.contrib.auth.forms import UserCreationForm

def home_page(request):
    return render(request, 'home/home_page.html')

def test(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            send_mail(form.cleaned_data['subject'], form.cleaned_data['content'],'stereotip.228@gmail.com', ['grinwich1211@mail.ru'])
            return redirect('./')
    else:
        form = ContactForm()
    return render(request, 'home/test.html', {"form": form})