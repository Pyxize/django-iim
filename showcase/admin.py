from django.contrib import admin
from .models import Person, Category, Article

# Register your models here.


admin.site.register(Person)
admin.site.register(Category)
admin.site.register(Article)