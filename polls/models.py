from django.conf import settings

from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class User_Blog(User):
    nick = models.CharField(max_length=30)
    about = models.TextField()

class User_Table(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    def get_url(self):
        return reverse("user-tab", kwargs={"id": self.id})

class Post(models.Model):
    add_date = models.DateTimeField(auto_now_add=True)
    mod_date = models.DateTimeField(auto_now=True)
    password = models.CharField(max_length=30, blank=True, null=True)
    title = models.CharField(max_length=100)
    limit = [
        ('P', 'Public'),
        ('Pr', 'Private'),
        ('H', 'Hidden'),
    ]
    contents = models.TextField()
    image = models.ImageField(upload_to="pictures", blank=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, default=1, on_delete=models.CASCADE)
    user_table = models.ForeignKey(User_Table, on_delete=models.CASCADE)
    def get_url(self):
        return reverse("post-detail", kwargs={"id": self.id})

class Comment(models.Model):
    add_date = models.DateTimeField(auto_now_add=True)
    mod_date = models.DateTimeField(auto_now=True)
    contents = models.TextField()
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)


