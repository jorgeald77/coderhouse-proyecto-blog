from django.contrib.auth.models import User
from django.db import models

from django.utils.timezone import now


class Profile(models.Model):
    name = models.CharField(max_length=74)
    image = models.ImageField(null=True, blank=True, upload_to='images/')
    description = models.TextField(null=True, blank=True)
    url = models.URLField(null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.PROTECT, null=True)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=32)

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=128)
    content = models.TextField()
    image = models.ImageField(null=True, blank=True, upload_to='images/')
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    published = models.DateField(null=True, blank=True)
    created = models.DateTimeField(default=now)
    author = models.ForeignKey(User, on_delete=models.PROTECT, null=True)

    def __str__(self):
        return self.title
