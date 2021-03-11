"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from showcase import views as showcase_views
from cv import views as cv_views

urlpatterns = [
    path('', cv_views.display_all, name='home'),
    path('admin/', admin.site.urls, name='admin'),
    path('showcase/', showcase_views.home, name='showcase'),
    path('showcase/members/', showcase_views.members, name='showcase.members'),
    path('showcase/contact/', showcase_views.contact, name='showcase.contact'),
    path('showcase/article/<int:article_id>/', showcase_views.article, name='showcase.article'),
    path('cv/', cv_views.home, name='cv'),
    path('cv/recruiters', cv_views.recruiters, name='cv.recruiters'),
]
