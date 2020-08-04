from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from .models import Animal, City, Species, Personality, Shelter, Partner, Reservation
import datetime


def index(request):
    template = loader.get_template('helpingpaw/index.html')
    context = {}
    return HttpResponse(template.render(context, request))

def animals(request):
    animal_list = Animal.objects.filter(adopted=False, reserved=False)
    context = {
        'animal_list': animal_list
    }
    return render(request, 'helpingpaw/animals.html', context)

def shelters(request):
    shelter_list = Shelter.objects.all()
    context = {
        'shelter_list': shelter_list,
    }
    return render(request, 'helpingpaw/shelters.html', context)

def partners(request):
    partner_list = Partner.objects.all()
    context = {
        'partner_list': partner_list
    }
    return render(request, 'helpingpaw/partners.html', context)

def animals_detail(request, animal_id):
    animal_detail = Animal.objects.get(pk=animal_id)
    age_gate = False
    if(animal_detail.age > 1):
        age_gate = True
    context = {
        'animal_detail': animal_detail,
        'age_gate': age_gate
    }
    return render(request, 'helpingpaw/animal_detail.html', context)

# def shelters_detail(request, shelter_id):
#     return HttpResponse('Shelter Detail')

# def partner_detail(request, partner_id):
#     return HttpResponse('Partner Detail')

def make_reservation(request, animal_id):
    animal_detail = Animal.objects.get(pk=animal_id, reserved=False, adopted=False)
    shelter_list = Shelter.objects.all()
    context = {
        'animal_detail': animal_detail,
        'shelter_list': shelter_list
    }
    return render(request, 'helpingpaw/make_reservation.html', context)

def reserve(request):
    animal = get_object_or_404(Animal, pk=request.POST['animal_id'])
    shelter = get_object_or_404(Shelter, pk=request.POST['shelter_id'])
    reservation = Reservation(first_name=request.POST['first_name'],last_name=request.POST['last_name'], email=request.POST['email'],reserved_animal=animal,reserved_shelter=shelter, reserved_date=request.POST['reservation_date'])
    reservation.save()
    animal.reserved = True
    animal.save()

    return HttpResponseRedirect(reverse('Reservation', args=[reservation.id]))

def reservation_detail(request, reservation_id):
    reservation = Reservation.objects.get(pk=reservation_id)
    date = datetime.date.isoformat(reservation.reserved_date)
    context = {
        'reservation': reservation,
        'date': date
    }
    return render(request, 'helpingpaw/reservation_detail.html', context)

def reservations_list(request):
    reservation_list = Reservation.objects.all()
    context = {
        'reservation_list': reservation_list
    }
    return render(request, 'helpingpaw/reservations_list.html', context)

def make_support(request):
    shelter_list = Shelter.objects.all()
    context = {
        'shelter_list': shelter_list
    }
    return render(request, 'helpingpaw/support_shelter.html', context)

def add_support(request):
    shelter = get_object_or_404(Shelter, pk=request.POST['shelter'])
    partner = Partner(name=request.POST['first_name']+' '+request.POST['last_name'], shelter_contributed_to=shelter,contribution=request.POST['support'],date_joined=datetime.date.today(), picture='/images/Thumbs_Up_Hand_Sign_Emoji_1024x1024.png')
    partner.save()

    return HttpResponseRedirect(reverse('Partners'))