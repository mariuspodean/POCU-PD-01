from django.shortcuts import render, redirect
from .models import Item
from distributors.models import Distributor



def all_items(request):
    items = Item.objects.all()
    return render(request, 'items/all_items.html', {'items':items})

def create_item(request):
    distributors = Distributor.objects.all
    
    if request.method == 'POST':
        title = request.POST['title']
        description = request.POST['description']
        quantity = request.POST['quantity']
        dist_name = request.POST['distributor']
        distributor = Distributor.objects.filter(title=dist_name).first()
        
        item = Item(title=title, description=description, quantity=quantity, distributor=distributor)
        
        item.save()
        return redirect('all_items')
    else:
        return render(request, 'items/create_item.html', {'distributors':distributors})
