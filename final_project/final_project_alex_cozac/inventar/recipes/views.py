from django.shortcuts import render, redirect
from .models import Recipe
from .models import Item

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

    

        item_title = request.POST['item_1']
        item_1 = Item.objects.filter(title=item_title).first()
        item_title = request.POST['item_2']
        item_2 = Item.objects.filter(title=item_title).first()
        item_title = request.POST['item_3']
        item_3 = Item.objects.filter(title=item_title).first()
        item_title = request.POST['item_4']
        item_4 = Item.objects.filter(title=item_title).first()
        item_title = request.POST['item_5']
        item_5 = Item.objects.filter(title=item_title).first()
        item_title = request.POST['item_6']
        item_6 = Item.objects.filter(title=item_title).first()
        item_title = request.POST['item_7']
        item_7 = Item.objects.filter(title=item_title).first()
        item_title = request.POST['item_8']
        item_8 = Item.objects.filter(title=item_title).first()

        image = request.FILES['img']

        if item_1:
            update_item(item_1)
        if item_2:
            update_item(item_2)
        if item_3:
            update_item(item_3)
        if item_4:
            update_item(item_4)
        if item_5:
            update_item(item_5)
        if item_6:
            update_item(item_6)
        if item_7:
            update_item(item_7)
        if item_8:
            update_item(item_8)

        recipe = Recipe(name=name, item_1=item_1, item_2=item_2, item_3=item_3, item_4=item_4, item_5=item_5, item_6=item_6, item_7=item_7, item_8=item_8, image=image)
        recipe.save()

        return redirect('all_recipes')
    else:
        return render(request, 'recipes/create_recipe.html', {'items':items})

def update_item(item):
    quantity = item.quantity-1
    Item.objects.filter(pk=item.id).update(quantity=quantity)
