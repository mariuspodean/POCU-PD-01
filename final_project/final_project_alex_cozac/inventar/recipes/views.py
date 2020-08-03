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

        image =  request.FILES

        recipe = Recipe(name=name, item1=item_1, item_2=item_2, item_3=item_3, item_4=item_4, item_5=item_5, item_6=item_6, item_7=item_7, item_8=item_8, image=image)
        recipe.save()

        return redirect('all_recipes')
    else:
        return render(request, 'recipes/create_recipe.html', {'items':items})

# def create_item(request):
#     distributors = Distributor.objects.all
    
#     if request.method == 'POST':
#         title = request.POST['title']
#         description = request.POST['description']
#         quantity = request.POST['quantity']
#         dist_name = request.POST['distributor']
#         distributor = Distributor.objects.filter(title=dist_name).first()
        
#         item = Item(title=title, description=description, quantity=quantity, distributor=distributor)
        
#         item.save()
#         return redirect('all_items')
#     else:
#         return render(request, 'items/create_item.html', {'distributors':distributors})
