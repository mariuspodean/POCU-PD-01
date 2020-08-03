from django.shortcuts import render
from .models import Recipe

def home(request):
    recipes = Recipe.objects.all()
    return render(request, 'recipes/home.html', {'recipes':recipes})

def all_recipes(request):
    recipes = Recipe.objects.all()
    return render(request, 'recipes/all_recipes.html', {'recipes':recipes})