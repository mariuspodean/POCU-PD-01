from django.shortcuts import render, redirect
from users.models import Walker, Gender, User, Owner, Review
from datetime import datetime
from django.views.generic import TemplateView, ListView, DetailView
from django.core.paginator import Paginator


class WalkerListingPageView(ListView):
    template_name = 'walkers.html'
    model = Walker
    paginate_by = 6


class WalkerDetailsPageView(DetailView):
    template_name= 'walker.html'
    pk_url_kwarg = 'walker_id'
    model = Walker

class MyLoginView(TemplateView):
    pass

def create_walker(request):
    if request.method == 'POST':
        name = request.POST['name']
        age = request.POST['age']
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        photo = request.FILES['photo']
        gender = Gender.FEMALE
        description = request.POST['description']
        walker = Walker(name=name, age=age, gender=gender, photo=photo, email=email, phone=phone, description=description)
        walker.save()
    return redirect('index')

def create_owner(request):
    if request.method == 'POST':
        name = request.POST['name']
        age = request.POST['age']
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        photo = request.FILES['photo']
        gender = Gender.FEMALE
        address = request.POST['address']
        owner = Owner(name=name, age=age, gender=gender, photo=photo, email=email, phone=phone, address=address)
        owner.save()
    return redirect('index')

def add_review(request):
    if request.method == 'POST':
        email = request.POST['email']
        review_text = request.POST['review_text']
        rating = int(request.POST.get('rating'))
        walker_id = request.POST['walker_idd']

        walker = Walker.objects.filter(pk=walker_id).first()
        owner = Owner.objects.filter(email=email).first()
        if owner:
            review = Review(walker=walker, review_text=review_text, rating=rating)
            review.save()
            final_rating = update_rating(walker.rating, rating)
            Walker.objects.filter(pk=walker_id).update(rating=final_rating)
    return redirect('/users/walkers/'+walker_id)


def update_rating(walker_rating, new_rating):
    return (walker_rating + new_rating) / 2