from django.db import models
from django import forms

# Create your models here.


SKILLS_CHOICES = (
    ("1", "Frontend"),
    ("2", "Backend"),
    ("3", "Full stack"),
    ("4", "Data Scientist"),
    ("5", "DevOps"),
)


TECHNOS_CHOICES = (
    ("1", "Javascript"),
    ("2", "Php"),
    ("3", "Python"),
    ("4", "Ruby"),
)


class CvForm(forms.Form):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email_address = models.EmailField(max_length=150)
    skills = forms.ChoiceField(choices=SKILLS_CHOICES)
    technologies = forms.ChoiceField(choices=TECHNOS_CHOICES)
