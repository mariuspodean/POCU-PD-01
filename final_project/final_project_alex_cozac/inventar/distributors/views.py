from django.shortcuts import render
from .models import Distributor

def all_distributors(request):
    distributors = Distributor.objects.all()
    return render(request, 'distributors/all_distributors.html', {'distributors':distributors})
