from django.contrib import admin

from .models import Realtor

class RealtorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'employee_of_month', 'email', 'hire_date')
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    list_editable = ('employee_of_month',)
    list_per_page = 10

admin.site.register(Realtor, RealtorAdmin)
