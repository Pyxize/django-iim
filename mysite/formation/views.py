from django.shortcuts import render
from .models import Article

# Create your views here.


def home(request):
    articles = Article.objects.all()
    return render(request, 'home/articles.html', {'articles': articles})


def members(request):
    return render(request, 'home/members.html')


def contact(request):
    return render(request, 'home/contact.html')



