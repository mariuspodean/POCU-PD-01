from django.urls import path
from . import views

urlpatterns = [
    # /HelpingPaw
    path('', views.index, name='index'),
    
    # /Animals
    path('Animals', views.animals, name='Animals'),

    # /Shelters
    path('Shelters', views.shelters, name='Shelters'),

    # /Partners
    path('Partners', views.partners, name='Partners'),

    # /Reservations
    path('Reservations', views.reservations_list, name='Reservations'),

    # /Animals/5
    path('Animals/<int:animal_id>', views.animals_detail, name='AnimalDetail'),

    # /HelpingPaw/Reserve
    path('Reserve/<int:animal_id>', views.make_reservation, name='MakeReservation'),

    # /HelpingPaw/Reservation
    path('Reservation', views.reserve, name='Reserve'),

    # /Reservation_Detail/5
    path('Reservation_Detail/<int:reservation_id>', views.reservation_detail, name='Reservation'),

    # /HelpingPaw/Reserve
    path('Support', views.make_support, name='SupportShelter'),

     # Adding SUpport
    path('AddSupport', views.add_support, name='AddSupport'),
    
]