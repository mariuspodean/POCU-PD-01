from django.urls import path
from . import views


urlpatterns = [
    path('all_recipes', views.all_recipes, name='all_recipes'),
    path('create_recipe', views.create_recipe, name='create_recipe'),
    path('update_items', views.update_items, name='update_items'),
]