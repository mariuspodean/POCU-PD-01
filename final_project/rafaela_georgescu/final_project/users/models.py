from django.db import models
from datetime import datetime

def user_directory_path(instance, filename): 
    return f'photos/users/user_{instance.name}/'


class Gender(models.TextChoices):
    FEMALE = 'F', 'Female'
    MALE = 'M', 'Male'
    OTHER = 'O', 'Other'


class User(models.Model):
    name = models.CharField(max_length=200)
    age = models.IntegerField()
    gender = models.CharField(max_length=1, choices=Gender.choices)
    photo = models.ImageField(upload_to=user_directory_path)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=50)
    date_added = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.name


class Walker(User):
    description = models.TextField(blank=True)
    rating = models.FloatField(default=0.0)


class Owner(User):
    address = models.TextField(max_length=200)


class Review(models.Model):
    walker = models.ForeignKey(Walker, on_delete=models.CASCADE)
    review_text = models.TextField(max_length=200)
    rating = models.IntegerField(default=0)

    def __str__(self):
        return self.review_text
