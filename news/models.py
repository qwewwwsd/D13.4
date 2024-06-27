from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


class NewsPost(models.Model):
    title = models.CharField(
        max_length=50,
        unique=True,
    )
    text = models.TextField(
        max_length=15000,
        unique=True
    )
    category = models.ForeignKey(
        to="Category",
        on_delete=models.CASCADE,
        related_name="newss",
    )
    dateCreation = models.DateTimeField(
        auto_now=True,
    )

    def __str__(self):
        return f"{self.title.title()} {self.text[:20]}..."
    
    def get_absolute_url(self):
        return reverse("newspost_detail", args=[str(self.id)])


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    subscribers = models.ManyToManyField(User, related_name='categories', through='Subscription')

    def __str__(self):
        return self.name.title()
    
    
class Subscription(models.Model):
    user = models.ForeignKey(
        to=User,
        on_delete=models.CASCADE,
        related_name='subscriptions',
    )
    category = models.ForeignKey(
        to='Category',
        on_delete=models.CASCADE,
        related_name='subscriptions',
    )
