from django.db import models
import datetime as dt
from django.conf import settings

# Create your models here.
class Task(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    time = models.DateTimeField(auto_now_add=True)


class Comments(models.Model):
    '''Comment model class '''
    comment = models.TextField()
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    task = models.ForeignKey(Task, on_delete=models.CASCADE)

    def __str__(self):
        return self.comment

    def save_comment(self):
        '''method  to save a comment'''
        self.save()

    def delete_comment(self):
        '''method to save a comment'''
        self.delete()

class Likes(models.Model):
    pass

class Bookmark(models.Model):
    pass
