from django.db import models
from django.core.files.storage import FileSystemStorage
from django import forms
from django.conf import settings
from django.db.models.signals import pre_delete

# Create your models here.

class UserOverview(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    total_balance = models.FloatField(default=0.0)
    total_transactions = models.FloatField(default=0.0)
    total_income = models.FloatField(default=0.0)
    total_expenses = models.FloatField(default=0.0)

    def __str__(self):
        return self.user.username


class Account(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    name = models.CharField(max_length=200)
    balance = models.FloatField()
    currency = models.CharField(max_length=30)

    def __str__(self):
        return self.name
    
    def delete(self, *args, **kwargs):

        user_overview = UserOverview.objects.get(user = self.user)
        user_overview.total_balance -= self.balance
       
        
        transactions = Transaction.objects.filter(account = self.id)
        for transaction in transactions:
            user_overview.total_transactions -= transaction.amount
            if transaction.transaction_type == 'Deposit':
                user_overview.total_income -= transaction.amount
            elif transaction.transaction_type == 'Withdraw':
                user_overview.total_expenses -= transaction.amount

        user_overview.save()
        super(Account, self).delete(*args, **kwargs)


class Category(models.Model):
    class Meta:
        verbose_name_plural = "categories"
        
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Transaction(models.Model):

    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    transaction_type = models.CharField(max_length=30)
    transaction_subtype = models.ForeignKey(Category, on_delete=models.CASCADE)
    amount = models.FloatField()
    date = models.DateField()
    comment = models.CharField(max_length=1000)

    def __str__(self):
        return self.transaction_subtype.name + ' - ' + self.account.currency + ' ' + str(self.amount)

    def delete(self, *args, **kwargs):

        account = Account.objects.get(pk=self.account.id)
        account.balance -= self.amount
        account.save()
        
        user_overview = UserOverview.objects.get(user = self.account.user)
        if self.transaction_type == 'Deposit':
            user_overview.total_balance -= self.amount
            user_overview.total_income -= self.amount
            user_overview.total_transactions -= self.amount
        elif self.transaction_type == 'Withdraw':
            user_overview.total_balance += self.amount
            user_overview.total_expenses -= self.amount
            user_overview.total_transactions -= self.amount
        user_overview.save()
        
        super(Transaction, self).delete(*args, **kwargs)
