from django.shortcuts import render

def about(request):
    return render(request, 'about/about_page.html')
# Create your views here.
