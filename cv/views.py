from django.shortcuts import render
from .models import CvForm

# Create your views here.


def display_all(request):
    return render(request, 'display.html')


def home(request):
    context = {}
    context['form'] = CvForm()
    return render(request, 'post_cv.html', context)


def recruiters(request):
    return render(request, 'display_cv.html')

