from django.urls import path

from pages import views


urlpatterns = [
    path('', views.PetListingPageView.as_view(), name='pets'),
    path('<int:pet_id>/', views.pet_details, name='pet_details')
]
