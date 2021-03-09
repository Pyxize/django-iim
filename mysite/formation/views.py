from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request, 'home/home.html')


def articles(request):
    return render(request, 'home/articles.html')


def members(request):
    return render(request, 'home/members.html')


def contact(request):
    return render(request, 'home/contact.html')



