from django.db import models
from django.contrib.auth.models import User, AbstractBaseUser, BaseUserManager,PermissionsMixin

# Create your models here.
class UserAccountManager(BaseUserManager):
	"""
	Helps Django work with our custom user model
	"""
	def create_user(self,email,username, password=None):
		"""
		Creates a new user profile object.
		"""

		if not email:
				raise ValueError('Users must have an email address')
		if not username:
				raise ValueError('Users must have a username')

		user = self.model(
			email=self.normalize_email(email),
			username=username,
		)

		user.set_password(password)
		user.save(using=self._db)

		return user

	def create_superuser(self, email, username, password):
		"""
		Creates and saves a new superuser with given deails
		"""
		user = self.create_user(
			email=self.normalize_email(email),
			password=password,
			username=username,
		)
		user.is_admin = True
		user.is_staff = True
		user.is_superuser = True

		user.save(using=self._db)

		return user


class Accounts(AbstractBaseUser,PermissionsMixin):
	"""Represents a "user profile" inside our system."""

	email			= models.CharField(max_length=100,verbose_name="email",unique=True)
	username		= models.CharField(max_length=100)
	date_joined		= models.DateTimeField(verbose_name='date joined',auto_now_add=True)
	last_login		= models.DateTimeField(verbose_name='last login',auto_now=True)
	is_admin		= models.BooleanField(default=False)
	is_active		= models.BooleanField(default=True)
	is_staff		= models.BooleanField(default=False)
	is_superuser	= models.BooleanField(default=False)

	objects = UserAccountManager()

	USERNAME_FIELD = 'email'
	REQUIRED_FIELDS = ['username']

	def __str__(self):
		"""Django uses this when it needs to convert the object to a string"""
		return self.email

	def get_full_name(self):
		"""used to get users full name."""

		return self.username

	def get_short_name(self):
		"""Used to get a users short name"""

		return self.username