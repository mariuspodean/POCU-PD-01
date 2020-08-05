from django.urls import path

from . import views

urlpatterns = [
    path('', views.costs, name='costs'),
    path('ingredients/', views.ingredients, name='ingredients'),
    path('recipes/', views.recipes, name='recipes'),
    path('add_ingredient/', views.add_ingredient, name='add_ingredient'),
    path('add_recipe/', views.add_recipe, name='add_recipe')
]