from django.db import models
from users.models import Walker
from pets.models import Pet
from datetime import datetime


class Appointment(models.Model):
    walker = models.ForeignKey(Walker, on_delete=models.DO_NOTHING)
    pet = models.ForeignKey(Pet, on_delete=models.DO_NOTHING)
    date = models.CharField(max_length=100)
    time = models.CharField(max_length=100)

    def __str__(self):
        return self.date + ' ' + self.time