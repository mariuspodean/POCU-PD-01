from django.db import models
import datetime


class Product(models.Model):
    # product_code = models.IntegerField()
    name = models.CharField(max_length=30)
    price = models.DecimalField(max_digits=5,decimal_places=2)
    quantity_available = models.IntegerField()

    def __str__(self):
        return self.name

class Customer(models.Model):
    # customer_code = models.IntegerField()
    customer_name = models.CharField(max_length=30)
    first_order = models.DateField()
    last_order = models.DateField()

    def __str__(self):
        return str(self.customer_name) 

class Order(models.Model):
    # order_code = models.IntegerField()
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    order_date = models.DateField()
    quantity = models.IntegerField()

    def __str__(self):
        return str(self.id)