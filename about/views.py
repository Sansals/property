from django.shortcuts import render

def about(request):
    email_None=''

    if request.user.is_authenticated:
        if request.user.email == '':
            email_None = 'Ограничено'

    data ={
        'email_None':email_None,
    }

    return render(request, 'about/about_page.html', data)
# Create your views here.
