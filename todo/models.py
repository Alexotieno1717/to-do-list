from django.db import models
import datetime as dt
from django.contrib.auth.models import User

# Create your models here.
class Task(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    time = models.DateTimeField(auto_add_now=True)


class Comments(models.Model):
    '''Comment model class '''
    comment = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
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
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    bookmark = models.TextField()

    def __str__(self):
        return self.bookmark

    def save_bookmark(self):
        self.save()

    def delete_bookmark(self):
        self.delete()



    
