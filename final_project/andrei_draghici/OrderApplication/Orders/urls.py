from django.contrib import admin
from django.urls import include, path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('orders/',views.orders,name='orders'),
    path('customers/',views.customers,name='customers'),
    path('products/',views.products,name='products'),
    path('orders/add_order',views.add_order,name='add_order'),
    path('products/add_product',views.add_product,name='add_product'),
    path('customers/add_customer',views.add_customer,name='add_customer'),
]