from django.urls import path

from .views import PetListingPageView, PetDetailsPageView, search, add_pet


urlpatterns = [
    path('', PetListingPageView.as_view(), name='pets'),
    path('<int:pet_id>/', PetDetailsPageView.as_view(), name='pet_details'),
    path('search', search, name='search'),
    path('add_pet', add_pet, name='add_pet')
]
