from django.shortcuts import render, redirect
from .models import Distributor

def all_distributors(request):
    distributors = Distributor.objects.all()
    return render(request, 'distributors/all_distributors.html', {'distributors':distributors})

def create_distributor(request):
    distributors = Distributor.objects.all()
    if request.method == 'POST':
        title = request.POST['title']
        description = request.POST['description']
        email = request.POST['email']
        phone = request.POST['phone']

        distributor = Distributor(title=title, description=description, email=email, phone=phone)
        distributor.save()
        return redirect('all_distributors')
    else:
        return render(request, 'distributors/create_distributor.html', {'distributors':distributors})