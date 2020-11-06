from django.db import models
import datetime as dt
from django.contrib.auth.models import User

# Create your models here.
class Task(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    time = models.DateTimeField(auto_add_now=True)


class Comments(models.Model):
    comment = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class TaskLikes(models.Model):
    likeusers = models.ManyToManyField(User)
    liketask = models.ForeignKey(Task,on_delete=models.CASCADE,null=True,related_name='liketask')

class Bookmark(models.Model):
    pass