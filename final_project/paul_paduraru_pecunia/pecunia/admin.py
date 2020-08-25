from django.contrib import admin
from .models import UserOverview, Account, Transaction, Category


admin.site.register(UserOverview)
admin.site.register(Account)
admin.site.register(Transaction)
admin.site.register(Category)