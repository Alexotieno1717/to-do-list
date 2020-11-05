from django.db import models
from django.contrib.auth.models import User, AbstractBaseUser

# Create your models here.
class Profile(AbstractBaseUser):
    username = models.CharField(max_length=100, unique=True)
    bio = models.TextField()
    email = models.CharField(max_length=100, verbose_name="email", unique=True)

    def __str__(self):
        return self.email