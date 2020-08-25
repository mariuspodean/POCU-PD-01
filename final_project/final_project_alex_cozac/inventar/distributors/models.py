from django.db import models


class Distributor(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=250)
    email = models.EmailField()
    phone = models.CharField(max_length=13)

    def __str__(self):
        return self.title
