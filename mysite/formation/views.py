from django.shortcuts import render
from .models import Article
from .models import Person

# Create your views here.


def home(request):
    articles = Article.objects.all()
    return render(request, 'home/articles.html', {'articles': articles})


def members(request):
    members = Person.objects.all()
    return render(request, 'home/members.html', {'members': members})


def contact(request):
    return render(request, 'home/contact.html')


def article(request, article_id):
    article = Article.objects.filter(id=article_id)
    return render(request, 'home/article.html', {"article": article[0], id: article_id})