from django.urls import path

from .views import add_appointment


urlpatterns = [
    path('add_appointment', add_appointment, name='add_appointment'),
]