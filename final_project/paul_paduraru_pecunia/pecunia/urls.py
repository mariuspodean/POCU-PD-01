from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from . import views
from django.conf.urls import url

urlpatterns = [
    path('', views.index_view, name='home'),
    path('login/', LoginView.as_view(), name='login_url'),
    path('register/', views.register_view, name='register_url'),
    path('logout/', LogoutView.as_view(next_page='home'), name='logout'),
    path('overview/', views.overview, name='overview'),
    path('overview/create_account/', views.create_account, name='create_account'),
    path('overview/create_transaction/', views.create_transaction, name='create_transaction'),
    url(r'^delete-account/(?P<pk>\d+)/$', views.delete_account, name='delete_account'),
    url(r'^delete-transaction/(?P<pk>\d+)/$', views.delete_transaction, name='delete_transaction')
]
