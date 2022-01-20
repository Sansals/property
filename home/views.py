from django.shortcuts import render

def home_page(request):
    email_None = ''
    if request.user.is_authenticated:
        if request.user.email == '':
            email_None = 'Ограничено'
    data = {
        'email_None': email_None,
    }
    return render(request, 'home/home_page.html', data)

def rules(request):
    email_None = ''
    if request.user.is_authenticated:
        if request.user.email == '':
            email_None = 'Ограничено'
    data = {
        'email_None': email_None,
    }
    return render(request, 'rules/rules.html', data)