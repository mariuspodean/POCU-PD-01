from django.urls import path

from . import views

from django.contrib.staticfiles.storage import staticfiles_storage
from django.views.generic.base import RedirectView

urlpatterns = [
    path('', views.index, name='index'),
    path('costs/', views.costs, name='costs'),
    path('ingredients/', views.ingredients, name='ingredients'),
    path('recipes/', views.recipes, name='recipes'),
    path('calculate_cost/', views.calculate_cost, name='calculate_cost'),
    path('add_ingredient/', views.add_ingredient, name='add_ingredient'),
    path('add_recipe/', views.add_recipe, name='add_recipe'),
]