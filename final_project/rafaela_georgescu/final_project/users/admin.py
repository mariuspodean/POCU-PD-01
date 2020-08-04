from django.contrib import admin

from .models import Walker, Owner, Review, User

admin.site.register(Walker)
admin.site.register(Owner)
admin.site.register(Review)
admin.site.register(User)

