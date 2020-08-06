from django.db import models
from datetime import datetime, date, timedelta
from django.utils import timezone

class Drugs(models.Model):
    name_of_drug = models.CharField(max_length=200, unique=True)
    data_of_expiration = models.DateTimeField('date_expiration')
    stock = models.IntegerField(default=0)

    def __str__(self):
        return self.name_of_drug

        
class Pacient(models.Model):
    name_pacient = models.CharField(max_length=200, unique=True)
    disease = models.CharField(max_length=200)
    email_address = models.EmailField(max_length=70,blank=True, null= True, unique= True)

    def __str__(self):
      return self.name_pacient + '-' + self.email_address
  
            
class Recipe(models.Model):
    date_of_renew = models.DateTimeField('date_of_renew')
    drugs = models.ManyToManyField(Drugs)
    name_pacient_recipe = models.ForeignKey(Pacient, on_delete=models.DO_NOTHING)
    

    def __str__(self):
      return '{}, {}'.format(
           self.date_of_renew, self.name_pacient_recipe)


