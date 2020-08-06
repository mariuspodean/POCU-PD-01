from django.shortcuts import render, redirect
from django.conf import settings
from django.contrib import messages
from pharm_tree.models import Pacient, Drugs, Recipe
from django.core.mail import send_mail
from datetime import datetime, date, timedelta
from .forms import AddPacientForm, AddDrugForm
import pytz
from django.core.paginator import Paginator

def home_page(request):
    return render(request, 'pharm_tree/home_page.html')

def drugs(request):
    list_drugs = Drugs.objects.all()
    paginator = Paginator(list_drugs, 10)
    page =request.GET.get('page')
    list_drugs = paginator.get_page(page)

    for dr in list_drugs:
        if dr.stock < 1:
            messages.warning(request, f' The stock is 0 for: {dr.name_of_drug}')

    date_2= datetime.utcnow().replace(tzinfo = pytz.utc) + timedelta(days=30)
    for exp in list_drugs:
        if exp.data_of_expiration < date_2:
             messages.warning(request, f'The {exp.name_of_drug} is nearly expired')

    return render(request, 'pharm_tree/drugs.html', {'list_drugs':list_drugs} )


def recipes(request):
    list_recipes = Recipe.objects.prefetch_related('drugs').all()
    date_of_renew_1 = datetime.utcnow().replace(tzinfo = pytz.utc) + timedelta(days=7)

    paginator = Paginator(list_recipes, 10)
    page =request.GET.get('page')
    list_recipes = paginator.get_page(page)

    for renew in list_recipes:
        if renew.date_of_renew < date_of_renew_1:
            messages.success(request, f'The recipe {renew.id} needs to be renew')
            messages.success(request, renew.name_pacient_recipe.email_address)
    
    return render(request, 'pharm_tree/recipes.html', {'list_recipes': list_recipes})

def pacients(request):   
    list_pacients = Pacient.objects.all()

    paginator = Paginator(list_pacients, 6)
    page =request.GET.get('page')
    list_pacients = paginator.get_page(page)

    form = AddPacientForm(request.POST or None)
    if form.is_valid():
            form.save()
            form = AddPacientForm()

    context = {
        'form': form,  
        'list_pacients' : list_pacients
    }
        
    return render(request, 'pharm_tree/pacients.html', context)

def contactus(request):
    return render(request, 'pharm_tree/contactus.html')

def addDrug(request):
    form = AddDrugForm()
    if request.method =='POST':
        form = AddDrugForm(request.POST or None)
        if form.is_valid():
                form.save()
                return redirect('/drugs')

    context = {
        'form': form
    }
    return render(request, 'pharm_tree/adddrug.html', context)

def editDrug(request, pk):
    edit_drug= Drugs.objects.get(id=pk)
    form = AddDrugForm(instance = edit_drug)

    if request.method == 'POST':   
        form = AddDrugForm(request.POST, instance=edit_drug)
        if form.is_valid():
                form.save()
                return redirect('/drugs')
    context ={
            'form': form
        }

    return render(request, 'pharm_tree/editdrug.html', context )
