from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.views.generic import TemplateView, ListView, DetailView
from pets.models import Pet, Gender, Size, Dog
from django.contrib import messages
from users.models import Owner

class PetListingPageView(TemplateView):
    template_name = 'pets.html'
    paginate_by = 6

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the genders
        context['genders'] = [Gender.MALE, Gender.FEMALE]
        # Add in a QuerySet of all the genders
        context['sizes'] = [Size.SMALL, Size.MEDIUM, Size.LARGE]
         # Add in a QuerySet of all the pets
        context['pets'] = Pet.objects.all()
        return context


class PetDetailsPageView(DetailView):
    template_name= 'pet.html'
    pk_url_kwarg = 'pet_id'
    model = Dog

def search(request):

    queryset_list = Dog.objects.order_by('-name')

    if 'keywords' in request.GET:
        keywords = request.GET['keywords']
        if keywords:
            queryset_list = queryset_list.filter(description__icontains=keywords)

    if 'gender' in request.GET:
        gender = request.GET['gender']
        if gender:
            queryset_list = queryset_list.filter(gender__iexact=Gender.MALE)

    if 'size' in request.GET:
        size = request.GET['size']
        if size:
            queryset_list = queryset_list.filter(size=Size.SMALL)
    
    if 'is_friendly_with_dogs' in request.GET:
       queryset_list = queryset_list.filter(is_friendly_with_dogs=True)

    if 'is_vaccinated' in request.GET:
       queryset_list = queryset_list.filter(is_vaccinated=True)

    if 'is_microchipped' in request.GET:
        queryset_list = queryset_list.filter(is_microchipped=True)

    context = {
        'pets':queryset_list,
        'values': request.GET,
        'genders': [Gender.MALE, Gender.FEMALE],
        'sizes': [Size.SMALL, Size.MEDIUM, Size.LARGE]
    }
    return render(request, 'pets.html', context)

def add_pet(request):
    if request.method == 'POST':
        name = request.POST['name']
        age = request.POST['age']
        gender = Gender.FEMALE
        size = Size.SMALL
        description = request.POST['description']
        main_photo = request.FILES['main_photo']
        owner = Owner.objects.filter(pk=request.user.id).first()
        breed = request.POST['breed']
        special_needs = request.POST['special_needs']
        is_neutered = request.POST.get('is_neutered', '') == 'on'
        is_vaccinated = request.POST.get('is_vaccinated', '') == 'on'
        is_friendly_with_dogs = request.POST.get('is_friendly_with_dogs', '') == 'on'
        is_friendly_with_cats = request.POST.get('is_friendly_with_cats', '') == 'on'
        is_friendly_with_kids = request.POST.get('is_friendly_with_kids', '') == 'on'
        is_microchipped = request.POST.get('is_microchipped', '') == 'on'

       
        dog = Dog(name=name, age=age, gender=gender, size=size, description=description, main_photo=main_photo, breed=breed, owner=owner, is_vaccinated=is_vaccinated, is_neutered=is_neutered, is_microchipped=is_microchipped, is_friendly_with_cats=is_friendly_with_cats, is_friendly_with_dogs=is_friendly_with_dogs, is_friendly_with_kids=is_friendly_with_kids, special_needs=special_needs)
        dog.save()
        messages.success(request, 'Dog added')
        return redirect('profile')
    return render(request, 'profile.html')