from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.views.generic import TemplateView, ListView, DetailView
from pets.models import Pet, Gender, Size, Dog

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