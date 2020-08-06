from django.urls import include, path
from .views import create_walker, create_owner, WalkerListingPageView, walker_details, add_review, login, logout, profile

urlpatterns = [
    path('create_walker', create_walker, name='create_walker'),
    path('create_owner', create_owner, name='create_owner'),
    path('login', login, name='login'),
    path('walkers/', WalkerListingPageView.as_view(), name='walkers'),
    path('walkers/<int:walker_id>/', walker_details, name='walker_details'),
    path('add_review', add_review, name='add_review'),
    path('logout', logout, name='logout'),
    path('profile', profile, name='profile')
]