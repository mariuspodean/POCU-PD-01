from django.http import HttpResponse
from django.shortcuts import redirect
from django.views.generic import TemplateView, ListView, DetailView
from pets.models import Pet
from users.models import Walker

class HomePageView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the walkers
        context['walkers'] = Walker.objects.all()
         # Add in a QuerySet of all the walkers
        context['pets'] = Pet.objects.all()
        return context


class AboutPageView(TemplateView):
    template_name = 'about.html'
