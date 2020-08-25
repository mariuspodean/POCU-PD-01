from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .models import UserOverview, Account, Transaction, Category
from pecunia.forms import CustomUserCreationForm, AccountForm, TransactionForm
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages


def index_view(request):
    if request.user.is_authenticated:
        redirect('overview')
    return render(request, 'home.html')


@login_required
def overview(request):
    """ Render User Overview, Accounts and Transactions for current user"""

    overview = UserOverview.objects.filter(user=request.user)
    accounts = Account.objects.filter(user=request.user)
    latest_transactions = Transaction.objects.filter(account__in=accounts)
    subtypes = Category.objects.order_by('name')
    total_amount = sum(
        transaction.amount for transaction in latest_transactions)

    if not overview:

        new_overview = UserOverview.objects.create(
            user=request.user,
            total_balance=0.0,
            total_transactions=0.0,
            total_income=0.0,
            total_expenses=0.0)

        context = {'overview': new_overview}
    else:
        context = {
            'overview': overview.first,
            'accounts': accounts,
            'latest_transactions': latest_transactions,
            'total_amount': total_amount,
            'subtypes': subtypes}

    return render(request, 'transactions/overview.html', context)


@login_required
def create_account(request):
    """ Create Accounts and update User View"""
    if request.method == 'POST':

        form = AccountForm(request.POST)

        if form.is_valid():

            form_name = form.cleaned_data['name']
            form_balance = form.cleaned_data['balance']
            form_currency = form.cleaned_data['currency']

            new_account = Account.objects.create(
                user=request.user, name=form_name, balance=form_balance, currency=form_currency)
            new_account.save()

            user_overview = UserOverview.objects.get(user=request.user)
            user_overview.total_balance += float(form['balance'].value())
            user_overview.save()

            return redirect('overview')

    else:
        form = AccountForm()

    return redirect('overview')


@login_required
def create_transaction(request):
    """ Create Transaction and update UserView and Account"""

    if request.method == 'POST':
        form = TransactionForm(request.POST)
        if form.is_valid():

            form_account = form.cleaned_data['account']
            form_transaction_type = form.cleaned_data['transaction_type']
            form_transaction_subtype = form.cleaned_data['transaction_subtype']
            form_amount = form.cleaned_data['amount']
            form_date = form.cleaned_data['date']
            form_comment = form.cleaned_data['comment']

            new_transaction = Transaction.objects.create(
                account=Account.objects.get(pk=form_account),
                transaction_type=form_transaction_type,
                transaction_subtype=Category.objects.get(
                    pk=form_transaction_subtype),
                amount=form_amount,
                date=form_date,
                comment=form_comment
            )
            new_transaction.save()

            new_account = Account.objects.get(pk=form_account)
            if form_transaction_type == 'Deposit':
                new_account.balance += form_amount
            elif form_transaction_type == 'Withdraw':
                new_account.balance -= form_amount
            new_account.save()

            user_overview = UserOverview.objects.get(user=request.user)
            user_overview.total_transactions += form_amount
            if form_transaction_type == 'Deposit':
                user_overview.total_balance += form_amount
                user_overview.total_income += form_amount
            elif form_transaction_type == 'Withdraw':
                user_overview.total_expenses += form_amount
                user_overview.total_balance -= form_amount
            user_overview.save()

            return redirect('overview')

    
    else:
        form = TransactionForm()


    return redirect('overview')


@login_required
def delete_account(request, pk):

    account = Account.objects.get(pk=pk)
    account.delete()

    return redirect('overview')


@login_required
def delete_transaction(request, pk):

    transaction = Transaction.objects.get(pk=pk)
    transaction.delete()

    return redirect('overview')


def register_view(request):
    
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login_url')
    else:
        form = CustomUserCreationForm()

    return render(request, 'registration/register.html', {'form': form})
