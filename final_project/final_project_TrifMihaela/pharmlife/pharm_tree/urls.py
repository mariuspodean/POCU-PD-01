from django.urls import path

from . import views

urlpatterns = [
    path('', views.home_page, name ='home_page'),
    path('drugs/', views.drugs, name ='drugs_page'),
    path('recipes/', views.recipes, name = 'recipes_page'),
    path('pacients/', views.pacients, name = 'pacients_page'),
    path('contactus/', views.contactus, name ='contactus_page'),
    path('drugs/adddrugs/', views.addDrug, name ='adddrugs_page'),
    path('drugs/editdrugs/<str:pk>/', views.editDrug, name ='editdrugs_page'),
]
