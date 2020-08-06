from django.shortcuts import render, redirect, get_object_or_404
from users.models import Walker, Gender, Owner, Review, User
from datetime import datetime
from django.views.generic import TemplateView, ListView, DetailView
from django.core.paginator import Paginator
from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
from django.db.models import F


class WalkerListingPageView(ListView):
    template_name = 'walkers.html'
    model = Walker
    paginate_by = 4


def walker_details(request, walker_id):
    walker = get_object_or_404(Walker, pk=walker_id)
    reviews = Review.objects.filter(walker=walker)
    context = {
        'walker': walker,
        'reviews': reviews
    }
    return render(request, 'walker.html', context)


def create_walker(request):
    if request.method == 'POST':
        name = request.POST['name']
        age = request.POST['age']
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        photo = request.FILES['photo']
        password = request.POST['password']
        gender = Gender.FEMALE
        description = request.POST['description']

        if User.objects.filter(email=email).exists():
            messages.error(request, 'Email already registered')
            return redirect('/users/create_walker')
        else:
            walker = Walker.objects.create_user(name=name, age=age, gender=gender, photo=photo, email=email, phone=phone, description=description, password=password)
            walker.save()
            messages.success(request, 'You are now registered')
            auth.login(request, walker)
            return redirect('profile')
    return render(request, 'index.html')

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
        password = request.POST['password']

        if User.objects.filter(email=email).exists():
            messages.error(request, 'Email already registered')
            return redirect('/users/walkers/')
        else:
            owner = Owner.objects.create_user(name=name, age=age, gender=gender, photo=photo, email=email, phone=phone, address=address, password=password)
            owner.save()
            messages.success(request, 'You are now registered')
            auth.login(request, owner)
            return redirect('profile')
    return render(request, 'index.html')
        
def add_review(request):
    if request.method == 'POST':
        review_text = request.POST['review_text']
        rating = int(request.POST.get('rating'))
        walker_id = request.POST['walker_idd']
        if request.user.is_authenticated:
            review_text = request.user.name.upper() + ': ' + review_text
        else:
            review_text = 'ANONYMOUS: ' + review_text
        
        walker = Walker.objects.filter(pk=walker_id).first()
        review = Review(walker=walker, review_text=review_text, rating=rating)
        review.save()
        update_rating(walker)

    return redirect('/users/walkers/'+walker_id)


def update_rating(walker):
    sum = 0
    walker_reviews = Review.objects.filter(walker=walker)
    reviews_no = walker_reviews.count()
    for review in walker_reviews:
        sum += review.rating
    Walker.objects.filter(pk=walker.id).update(rating=sum / reviews_no)


def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = auth.authenticate(email=email, password=password)
        if user is not None:
            auth.login(request, user)
            messages.success(request, 'You are now logged in')
            return redirect('profile')
        else:
            messages.error(request, 'Wrong credentials')
            return redirect('login')
    return render(request, 'index.html')


def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        messages.success(request, 'You are now logged out')
    return redirect('index')


@login_required(login_url='/users/login/')
def profile(request):
    # user_inquiries = Inquiry.objects.order_by('-inquiry_date').filter(user_id=request.user.id)
    # context = {
    #     'inquiries' : user_inquiries
    # }
    # return render(request, 'accounts/dashboard.html', context)
    return render(request, 'profile.html')
