from django.contrib import admin
from .models import Drugs, Pacient, Recipe

admin.site.register(Drugs)
admin.site.register(Pacient)
admin.site.register(Recipe)
