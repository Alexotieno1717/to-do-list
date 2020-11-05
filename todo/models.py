from django.db import models
import datetime as dt
from django.contrib.auth.models import User

# Create your models here.
class Task(models.Model):
    title = models.CharField(max_length=100, blank=True, default='')
    description = models.TextField()
    time = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey('auth.User', related_name='snippets', on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Comments(models.Model):
    comment = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class Likes(models.Model):
    pass

class Bookmark(models.Model):
    pass