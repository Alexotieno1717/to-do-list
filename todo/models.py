from django.db import models
import datetime as dt
from django.contrib.auth.models import User

# Create your models here.
class Task(models.Model):
    title = models.CharField(max_length=100, blank=True, default='')
    description = models.TextField()
    time = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey('auth.User', null=True, related_name='snippets', on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Comments(models.Model):
    '''Comment model class '''
    comment = models.TextField()
    owner = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    task = models.ForeignKey(Task, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.comment

    def save_comment(self):
        '''method  to save a comment'''
        self.save()

    def delete_comment(self):
        '''method to save a comment'''
        self.delete()

class TaskLikes(models.Model):
    likeusers = models.ManyToManyField(User)
    liketask = models.ForeignKey(Task, on_delete=models.CASCADE,null=True,related_name='liketask')

class Bookmark(models.Model):
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    task = models.ForeignKey(Task, null=True, on_delete=models.CASCADE)
    bookmark = models.TextField()

    def __str__(self):
        return self.bookmark

    def save_bookmark(self):
        self.save()

    def delete_bookmark(self):
        self.delete()



    
