from django.shortcuts import render, redirect
from .models import Article
from .models import Person, ContactForm

from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from django.contrib import messages

# Create your views here.


def home(request):
    articles = Article.objects.all()
    return render(request, 'home/articles.html', {'articles': articles})


def members(request):
    members = Person.objects.all()
    return render(request, 'home/members.html', {'members': members})


def article(request, article_id):
    article = Article.objects.filter(id=article_id)
    return render(request, 'home/article.html', {'article': article[0], id: article_id})


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = 'Bulma R&D'
            body = {
                'first_name': form.cleaned_data['first_name'],
                'last_name': form.cleaned_data['last_name'],
                'email': form.cleaned_data['email_address'],
                'message': form.cleaned_data['message'],
            }
            message = "\n".join(body.values())

            try:
                send_mail(subject, message, 'antoinemaurel6@gmail.com', ['antoinemaurel6@gmail.com'])
                messages.success(request, 'Form submission successful')
            except BadHeaderError:
                return HttpResponse('Invalid header found.')

            return redirect('/')
      
    form = ContactForm()
    return render(request, 'home/contact.html', {'form': form})
