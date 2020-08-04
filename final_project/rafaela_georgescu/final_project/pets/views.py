from django.http import HttpResponse
from django.shortcuts import redirect
from django.views.generic import TemplateView, ListView, DetailView
from pets.models import Pet

class PetListingPageView(ListView):
    template_name = 'pets.html'
    model = Pet
    paginate_by = 6


class PetDetailsPageView(DetailView):
    template_name= 'pet.html'
    pk_url_kwarg = 'pet_id'
    model = Pet