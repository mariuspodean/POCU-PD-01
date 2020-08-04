from django.urls import include, path
from .views import create_walker, create_owner, WalkerListingPageView, WalkerDetailsPageView, add_review

urlpatterns = [
    path('create_walker', create_walker, name='create_walker'),
    path('create_owner', create_owner, name='create_owner'),
    path('walkers/', WalkerListingPageView.as_view(), name='walkers'),
    path('walkers/<int:walker_id>/', WalkerDetailsPageView.as_view(), name='walker_details'),
    path('add_review', add_review, name='add_review')
]