from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import UserOverview, Account, Transaction, Category
from django.core.exceptions import ValidationError

class CustomUserCreationForm(forms.Form):
    username = forms.CharField(label='Enter username', min_length=4, max_length=150)
    email = forms.EmailField(label='Enter email')
    password1 = forms.CharField(label='Enter password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirm password', widget=forms.PasswordInput)

    def clean_username(self):
        username = self.cleaned_data['username'].lower()
        r = User.objects.filter(username=username)
        if r.count():
            raise  ValidationError("Username already exists")
        return username

    def clean_email(self):
        email = self.cleaned_data['email'].lower()
        r = User.objects.filter(email=email)
        if r.count():
            raise  ValidationError("Email already exists")
        return email

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if password1 and password2 and password1 != password2:
            raise ValidationError("Password don't match")

        return password2

    def save(self, commit=True):
        user = User.objects.create_user(
            self.cleaned_data['username'],
            self.cleaned_data['email'],
            self.cleaned_data['password1'],
        )
        return user

class AccountForm(forms.Form):
    name = forms.CharField(max_length=200)
    balance = forms.FloatField()
    currency = forms.CharField(max_length=30)
    
class TransactionForm(forms.Form):
    account = forms.IntegerField()
    transaction_type = forms.CharField()
    transaction_subtype = forms.IntegerField()
    amount = forms.FloatField()
    date = forms.DateField()
    comment = forms.CharField(max_length=1000)
    