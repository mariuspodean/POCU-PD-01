from django.http import HttpResponse
from django.views.generic import TemplateView


class HomePageView(TemplateView):
    template_name = 'index.html'


class AboutPageView(TemplateView):
    template_name = 'about.html'


class PetListingPageView(TemplateView):
    template_name = 'pets.html'


def pet_details(pet_id):
    return HttpResponse(f'For fuck\'s sake! {pet_id}')
