from django.db import models

# Create your models here.


class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    role = models.CharField(max_length=100)
    born_date = models.DateField()

    @property
    def full_name(self):
        "Returns the person's full name."
        return '%s %s' % (self.first_name, self.last_name)


class Category(models.Model):
    name = models.CharField(max_length=30)
    parent = models.ForeignKey(
        'self', blank=True,
        null=True,
        related_name='child',
        on_delete=models.CASCADE
    )


class Article(models.Model):
    name = models.CharField(max_length=30)
    content = models.CharField(max_length=400)
    category = models.ForeignKey('Category', null=True, on_delete=models.CASCADE)
