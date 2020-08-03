from django.db import models
from distributors.models import Distributor


class Item(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=250)
    quantity = models.IntegerField()
    
    distributor = models.ForeignKey(Distributor, on_delete = models.CASCADE)

    def __str__(self):
        return self.title