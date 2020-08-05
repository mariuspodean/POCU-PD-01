from django.db import models
from datetime import datetime
import os
from django.contrib.auth.models import AbstractUser, BaseUserManager

def user_directory_path(instance, filename): 
    print(f'DEBUG: instance name {instance.name}')
    print(f'DEBUG: filename {filename}')
    return os.path.join(
        'photos/users/',
        instance.name,
        filename
    )

class Gender(models.TextChoices):
    FEMALE = 'F', 'Female'
    MALE = 'M', 'Male'
    OTHER = 'O', 'Other'

class UserManager(BaseUserManager):
    """Define a model manager for User model with no username field."""

    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        """Create and save a User with the given email and password.."""
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        """Create and save a regular User with the given email and password."""
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        """Create and save a SuperUser with the given email and password."""
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('age', 100)
        extra_fields.setdefault('gender', Gender.OTHER)
        extra_fields.setdefault('photo', None)
        extra_fields.setdefault('phone', "111111111")

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, password, **extra_fields)
class User(AbstractUser):
    name = models.CharField(max_length=200)
    email = models.EmailField(unique=True)
    age = models.IntegerField()
    gender = models.CharField(max_length=1, choices=Gender.choices, default=Gender.FEMALE)
    photo = models.ImageField(upload_to=user_directory_path)
    phone = models.CharField(max_length=50)
    date_added = models.DateTimeField(default=datetime.now)
    password = models.CharField(max_length=50, default="password")

    username = None

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.name

    objects = UserManager()


class Walker(User):
    description = models.TextField(blank=True)
    rating = models.FloatField(default=0.0)

    class Meta:
        verbose_name = "Walker"


class Owner(User):
    address = models.TextField(max_length=200)

    class Meta:
        verbose_name = "Owner"


class Review(models.Model):
    walker = models.ForeignKey(Walker, on_delete=models.DO_NOTHING)
    review_text = models.TextField(max_length=200)
    rating = models.IntegerField(default=0)

    def __str__(self):
        return self.review_text
