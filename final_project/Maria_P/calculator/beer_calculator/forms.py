from django import forms
from django.forms import ModelForm

from .models import IngredientType, Ingredient, RecipeType, Recipe, Cost

class AddIngredientForm(ModelForm):
    class Meta:
        model = Ingredient
        fields = ['name', 'ingredient_type', 'quantity', 'price', 'update_date_time']

class AddRecipeForm(ModelForm):
    class Meta:
       model = Recipe
       fields = ['name', 'recipe_type', 'ingredients', 'update_date_time']

class CalculateCostForm(ModelForm):
    class Meta:
        model = Cost
        fields = ['recipe', 'ingredient', 'quantity', 'date_time']