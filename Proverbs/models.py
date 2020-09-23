from django.conf import settings
from django.db import models
from django.utils import timezone


# Create your models here.
class Proverb(models.Model):
    PROVERB_OPTIONS = [
        ('SALARY', 'SALARY'),
        ('BUSINESS', 'BUSINESS'),
        ('SIDE-HUSTLES', 'SIDE-HUSTLES'),
        ('OTHERS', 'OTHERS')
    ]

    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = models.TextField()
    category = models.CharField(choices=PROVERB_OPTIONS, max_length=255)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.content


class Interpretation(models.Model):
    language = models.CharField(max_length=100, default=None)
    content = models.TextField(default=None)
    proverb = models.ForeignKey(Proverb, null=True, on_delete=models.SET_NULL, related_name='interpretation')
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.content

class Translation(models.Model):
    language = models.CharField(max_length=100, default=None)
    content = models.TextField(default=None)
    proverb = models.ForeignKey(Proverb, null=True, on_delete=models.SET_NULL, related_name='translation')
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.content

class Ethnic(models.Model):
    name = models.CharField(max_length=100, default=None)
    language = models.CharField(max_length=100, default=None)
    state = models.CharField(max_length=100, default=None)
    proverb = models.ForeignKey(Proverb, null=True, on_delete=models.SET_NULL, related_name='ethnic')
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name