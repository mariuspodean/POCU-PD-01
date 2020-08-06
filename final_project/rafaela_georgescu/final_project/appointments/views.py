from django.shortcuts import render, get_object_or_404
from users.models import Walker
from pets.models import Pet
from .models import Appointment
from django.contrib import messages

# Create your views here.
def add_appointment(request):
    if request.method == 'POST':
        walker = get_object_or_404(Walker, pk=request.user.pk)
        pet = Pet.objects.get(pk=request.POST['pet_id'])
        time = request.POST['times']
        date = request.POST['dates']

        appointment = Appointment(walker=walker, pet=pet, date=date, time=time)
        appointment.save()
        messages.success(request, 'Appointment created')
        # return redirect('profile')
    return render(request, 'profile.html')