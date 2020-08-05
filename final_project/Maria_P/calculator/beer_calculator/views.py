from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

from .models import IngredientType, Ingredient, RecipeType, Recipe, Cost

from .forms import AddIngredientForm, AddRecipeForm, CalculateCostForm


def ingredients(request):
    ingredients_list = Ingredient.objects.order_by('name')
    context = {'ingredients_list': ingredients_list}
    return render(request, 'beer_calculator/ingredients.html', context)

def add_ingredient(request):
    if request.method == 'POST':
        form = AddIngredientForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('ingredients'))
    else:
        form = AddIngredientForm()
    return render(request, 'beer_calculator/add_ingredient.html', {'form': form})


def recipes(request):
    recipes_list = Recipe.objects.order_by('name')
    context = {'recipes_list': recipes_list}
    return render(request, 'beer_calculator/recipes.html', context)

def add_recipe(request):
    if request.method == 'POST':
        form = AddRecipeForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('recipes'))
    else:
        form = AddRecipeForm()
    return render(request, 'beer_calculator/add_recipe.html', {'form': form})

def costs(request):
    costs_list = Cost.objects.order_by('recipe')
    context = {'costs_list': costs_list}
    return render(request, 'beer_calculator/costs.html', context)

def calc_cost(x, y):
    return (x * y)/100

def calculate_cost(request):
    if request.method == 'POST':
        form = CalculateCostForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.cost = calc_cost(instance.ingredient.price, instance.quantity)
            instance.save()
            return HttpResponseRedirect(reverse('costs'))
    else:
        form = CalculateCostForm()
    return render(request, 'beer_calculator/calculate_cost.html', {'form': form})