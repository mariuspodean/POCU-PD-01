from django.urls import path
from . import views


urlpatterns = [
    path('all_distributors', views.all_distributors, name='all_distributors'),
    path('create_distributor', views.create_distributor, name='create_distributor'),
]