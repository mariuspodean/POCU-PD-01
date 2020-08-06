from django.shortcuts import render,redirect
from .models import Product, Order, Customer
from datetime import datetime

def index(request):
    return render(request,'index.html')

def products(request):
    products_list = Product.objects.filter(quantity_available__gt=0)
    context = {
        'products':products_list
    }
    return render(request,'products.html',context)

def orders(request):
    today = datetime.now()
    orders_list = Order.objects.all().filter(order_date__year=today.year)
    customer_list = Customer.objects.all()
    product_list = Product.objects.filter(quantity_available__gt=0)

    context = {
        'orders':orders_list,
        'customers':customer_list,
        'products':product_list
    }
    return render(request,'orders.html',context)

def customers(request):
    customers_list = Customer.objects.order_by('customer_name')
    context = {
        'customers':customers_list
    }
    return render(request,'customers.html',context)

def add_order(request):
    if request.method=='POST':
        customer = Customer.objects.filter(customer_name=request.POST['customer']).first()
        product = Product.objects.filter(name=request.POST['product']).first()
        order_date = datetime.now()
        quantity = request.POST['quantity']
        order = Order(customer=customer,product=product,order_date=order_date,quantity=quantity)
        order.save()
    return redirect('orders')


def add_customer(request):
    if request.method=='POST':
        customer_name = request.POST['customer_name']
        first_order = datetime.now()
        last_order = datetime.now()
        customer = Customer(customer_name=customer_name,first_order = first_order, last_order = last_order)
        customer.save()
    return redirect('customers')


def add_product(request):
    if request.method=='POST':
        name = request.POST['name']
        price = int(request.POST['price'])
        quantity = int(request.POST['quantity'])
        name = Product(name=name,price=price,quantity_available=quantity)
        name.save()
    return redirect('products')