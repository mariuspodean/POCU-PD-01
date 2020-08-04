from django.db import models

class Ingredient_Type(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Ingredient(models.Model):
    name = models.CharField(max_length=200)
    ingredient_type = models.ForeignKey(Ingredient_Type, on_delete=models.PROTECT)
    quantity = models.DecimalField('Quantity (g)', max_digits=10, decimal_places=2)
    price = models.DecimalField('Price for 100 g (RON)', max_digits=10, decimal_places=2)
#    add_date = models.DateTimeField('date added')
    update_date = models.DateTimeField('date updated')

    def __str__(self):
        return self.name

class Recipe_Type (models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Recipe(models.Model):
    name = models.CharField(max_length=200)
    recipe_type = models.ForeignKey(Recipe_Type, on_delete=models.PROTECT)
    ingredient = models.ManyToManyField(Ingredient)
 #   ingredient = models.ForeignKey(Ingredient, on_delete=models.PROTECT)
 #   quantity = models.DecimalField(max_digits=10, decimal_places=2)
 #   add_date = models.DateTimeField('date added')
    update_date = models.DateTimeField('date updated')

    def __str__(self):
        return self.name

class Cost(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    cost = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f'{self.recipe} - {self.ingredient}'
