from django.contrib import admin

from .models import Ingredient_Type, Ingredient, Recipe_Type, Recipe, Cost

admin.site.register(Ingredient_Type)
admin.site.register(Ingredient)
admin.site.register(Recipe_Type)
admin.site.register(Recipe)
admin.site.register(Cost)
