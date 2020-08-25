from django.shortcuts import render, redirect
from .models import Recipe
from .models import Item
from django.db.models import F

def home(request):
    recipes = Recipe.objects.all()
    return render(request, 'recipes/home.html', {'recipes':recipes})

def all_recipes(request):
    recipes = Recipe.objects.all()
    return render(request, 'recipes/all_recipes.html', {'recipes':recipes})


def create_recipe(request):
    items = Item.objects.all()

    if request.method == 'POST':
        name = request.POST['name']
        item_titles = request.POST.getlist('select-items')
        
        image = request.FILES['img']
        recipe = Recipe.objects.create(name=name, image=image)
        
        recipe.save()
        for item_title in item_titles:
            recipe.items.add(Item.objects.filter(title=item_title).first())
        return redirect('all_recipes')
    else:
        return render(request, 'recipes/create_recipe.html', {'items':items})

def update_items(request):
    recipe_id = int(request.POST.get("recipe_id")) 
    recipe = Recipe.objects.filter(pk=recipe_id).first()
    recipe.items.update(quantity=F("quantity")-1)

    return redirect('all_items')