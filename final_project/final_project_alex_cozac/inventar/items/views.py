from django.shortcuts import render
from .models import Item
from distributors.models import Distributor


def all_items(request):
    items = Item.objects.all()
    return render(request, 'items/all_items.html', {'items':items})

def create_item(request):
    # distributors = Distributor.objects.all()

    if request.method == 'POST':
        title = request.POST['title']
        description = request.POST['description']
        quantity = request.POST['quantity']
        distributor = Distributor.objects.get(request.POST['distributor'])
        
        
        item = Item(title=title, description=description, quantity=quantity, distributor=distributor)
        
        item.save()
    
    items = Item.objects.all()
    return render(request, 'items/create_item.html', {'items':items})


# def createItem(request):
#     if request.method == 'POST':
#         if request.POST.get('title') and request.POST.get('descritpion') and request.POST.get('quantity') and request.POST.get('distributor'):
#             post=Item()
#             post.title = request.POST.get('title')
#             post.description = request.POST.get('description')
#             post.quantity = request.POST.get('quantity')
#             post.distributor = request.POST.get('distributor')
#             post.save()


#             return render(request, 'create_item.html')
#     else:
#             return render(request, 'create_item.html')
# def createItem(request):
#     if request.method == 'POST':
#         title = request.POST['title']
#         description = request.POST['description']
#         quantity = request.POST['quantity']
#         distributor = request.POST['distributor']
        
#         item = Item(title = title, description=description, quantity=quantity, distributor=distributor)
 
#         item.save()
#         return 