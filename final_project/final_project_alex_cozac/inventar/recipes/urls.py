from django.urls import path
from . import views


urlpatterns = [
    path('all_recipes', views.all_recipes, name='all_recipes'), 
]