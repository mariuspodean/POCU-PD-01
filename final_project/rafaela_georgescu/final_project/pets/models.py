from django.db import models
from datetime import datetime
from users.models import Owner
import os


def pet_directory_path(instance, filename): 
    return os.path.join(
        'photos/pets/',
        instance.name,
        filename
    )

class Gender(models.TextChoices):
    FEMALE = 'F', 'Female'
    MALE = 'M', 'Male'


class Size(models.TextChoices):
    SMALL = 'S', 'Small'
    MEDIUM = 'M', 'Medium'
    LARGE = 'L', 'Large'


class Pet(models.Model):
    name = models.CharField(max_length=200)
    age = models.IntegerField()
    size = models.CharField(max_length=1, choices=Size.choices)
    gender = models.CharField(max_length=1, choices=Gender.choices)
    description = models.TextField(blank=True)
    date_added = models.DateTimeField(default=datetime.now)
    main_photo = models.ImageField(upload_to=pet_directory_path)
    photo_1 = models.ImageField(upload_to=pet_directory_path, blank=True)
    photo_2 = models.ImageField(upload_to=pet_directory_path, blank=True)
    owner = models.ForeignKey(Owner, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.name


class Dog(Pet):
    breed = models.CharField(max_length=200, blank=True)
    special_needs = models.TextField(blank=True)
    is_neutered = models.BooleanField(default=False)
    is_vaccinated = models.BooleanField(default=False)
    is_friendly_with_dogs = models.BooleanField(default=False)
    is_friendly_with_cats = models.BooleanField(default=False)
    is_friendly_with_kids = models.BooleanField(default=False)
    is_microchipped = models.BooleanField(default=False)
