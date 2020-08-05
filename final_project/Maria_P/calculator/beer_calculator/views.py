from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

from .models import Ingredient_Type, Ingredient, Recipe_Type, Recipe, Cost

from .forms import Add_Ingredient_Form, Add_Recipe_Form


def ingredients(request):
    ingredients_list = Ingredient.objects.order_by('name')
    context = {'ingredients_list': ingredients_list}
    return render(request, 'beer_calculator/ingredients.html', context)

def add_ingredient(request):
    if request.method == 'POST':
        form = Add_Ingredient_Form(request.POST)
        if form.is_valid():
            new_ingredient = Ingredient()
            new_ingredient.name = form.cleaned_data['name']
            new_ingredient.ingredient_type = form.cleaned_data['ingredient_type']
            new_ingredient.quantity = form.cleaned_data['quantity']
            new_ingredient.price = form.cleaned_data['price']
#           new_ingredient.add_date = form.cleaned_data['add_date']
            new_ingredient.update_date = form. cleaned_data['update_date']
            new_ingredient.save()
            return HttpResponseRedirect(reverse('ingredients'))
    else:
        form = Add_Ingredient_Form()
    return render(request, 'beer_calculator/add_ingredient.html', {'form': form})


def recipes(request):
    recipes_list = Recipe.objects.order_by('name')
    context = {'recipes_list': recipes_list}
    return render(request, 'beer_calculator/recipes.html', context)

def add_recipe(request):
    if request.method == 'POST':
        form = Add_Recipe_Form(request.POST)
        if form.is_valid():
            new_recipe = Recipe()
            new_recipe.name = form.cleaned_data['name']
            new_recipe.recipe_type = form.cleaned_data['recipe_type']
            new_recipe.ingredient = form.cleaned_data['ingredient']
 #           returned_quesryset = form.cleaned_data['ingredient']
  #          for item in returned_quesryset.iterator():
   #             new_recipe.ingredient.add(item)
 #           new_recipe.quantity = form.cleaned_data['quantity']
 #           new_recipe.add_date = form.cleaned_data['add_date']
            new_recipe.update_date = form. cleaned_data['update_date']
            new_recipe.save()
            return HttpResponseRedirect(reverse('recipes'))
    else:
        form = Add_Recipe_Form()
    return render(request, 'beer_calculator/add_recipe.html', {'form': form})

def costs(request):
    return HttpResponse("These are the costs for your recipe")