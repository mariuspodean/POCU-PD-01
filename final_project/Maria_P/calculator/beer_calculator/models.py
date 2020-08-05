from django.db import models
from datetime import datetime

class IngredientType(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Ingredient(models.Model):
    name = models.CharField(max_length=200)
    ingredient_type = models.ForeignKey(IngredientType, on_delete=models.PROTECT)
    quantity = models.DecimalField('Quantity (g)', max_digits=10, decimal_places=2)
    price = models.DecimalField('Price for 100 g (RON)', max_digits=10, decimal_places=2)
    update_date_time = models.DateTimeField('Update Date & Time', default=datetime.now)

    def __str__(self):
        return self.name

class RecipeType (models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Recipe(models.Model):
    name = models.CharField(max_length=200)
    recipe_type = models.ForeignKey(RecipeType, on_delete=models.PROTECT)
    ingredients = models.ManyToManyField(Ingredient)
    update_date_time = models.DateTimeField('Update Date & Time', default=datetime.now)

    def __str__(self):
        return self.name

class Cost(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    quantity = models.DecimalField('Quantity (g)', max_digits=10, decimal_places=2)
    date_time = models.DateTimeField('Date & Time', default=datetime.now)
    cost = models.DecimalField(editable=False, default=0, max_digits=10, decimal_places=2)

    def __str__(self):
        return f'{self.recipe} - {self.ingredient}'
