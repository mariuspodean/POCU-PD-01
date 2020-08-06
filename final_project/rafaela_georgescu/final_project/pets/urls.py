from django.urls import path

from .views import PetListingPageView, PetDetailsPageView, search


urlpatterns = [
    path('', PetListingPageView.as_view(), name='pets'),
    path('<int:pet_id>/', PetDetailsPageView.as_view(), name='pet_details'),
    path('search', search, name='search')
]
