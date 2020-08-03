from django.contrib import admin

from .models import Inquiry

class InquiryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'listing', 'email', 'inquiry_date')
    list_display_links = ('id', 'name', 'listing', 'email')
    search_fields = ('name', 'email', 'listing')
    list_per_page = 10


admin.site.register(Inquiry, InquiryAdmin)
