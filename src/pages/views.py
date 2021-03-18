from django.shortcuts import render, redirect
from .models import Product, Contact, Newsletter
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.urls import reverse 
import stripe
stripe.api_key = "sk_test_51IWG0lBCYGTfkEON6khkDlJ72yM9Mt8k07dWzbJZFjKtJFFtHYIzUvd7bFj9R3aVkEMCF13SJLOyRSWEmcPijh3600imVcQTB2"

# Create your views here.
def index_view(request):
    product_list = Product.objects.all()
    return render(request, 'pages/index.html', {'product_list':product_list, 'heading': 'Casual Shoes for Men', 'trending': True, 'btn':True})

def about_view(request):
    return render(request, 'pages/about.html', { 'heading': 'About Us'})

def blog_view(request):
    return render(request, 'pages/blog.html', { 'heading': 'Blog Page'})

def contact_view(request):
    if request.method == 'POST':
        name = request.POST['Name']
        email = request.POST['Email']
        phone = request.POST['Phone']
        message = request.POST['Message']
        obj = Contact.objects.create(name=name, email=email, phone=phone, message=message)
        obj.save()
        messages.success(request, 'Request Sent.')
        return redirect('/')

    return render(request, 'pages/contact.html', { 'heading': 'Contact Us'})

def newsletter_view(request):
    if request.method == 'POST':
        email = request.POST['Email']
        obj = Newsletter.objects.create(email=email)
        obj.save()
        messages.success(request, 'Request Sent.')
        return redirect('/')

    return render(request, 'pages/contact.html', { 'heading': 'Contact Us'})


def single_view(request):
    return render(request, 'pages/single.html', { 'heading': 'Blog'})

def shop_list_view(request):
    filter_capsules = []

    product_list = Product.objects.all()[:5]
    qs = Product.objects.all()
    total_products = len(qs)
    name = request.GET.get('name')
    price = request.GET.get('price')
    tags = request.GET.get('tags')
    if name != '' and name is not None:
        filter_capsules.append(('Product name: ' + str(name)))
    if price != '' and price is not None:
        filter_capsules.append(('Price: ' + '< ' + str(price)))
    if tags != '' and tags is not None:
        filter_capsules.append(('Occasion: ' + str(tags)))
    print(filter_capsules)
    if name is not None and name != '':
        qs = qs.filter(name__icontains=name)

    if price is not None and price != '':
        qs = qs.filter(price__lte=price)

    if tags is not None and tags != '':
        qs = qs.filter(tags__name__icontains=tags)

    filtered_products = len(qs)


    return render(request, 'pages/shop.html', {'filter': qs, 'heading':'Shop', 'product_list': product_list, 'total_products': total_products, 'filtered_products': filtered_products, 'filter_capsules':filter_capsules})
    # return render(request, 'pages/shop.html', {'heading': 'Shop'})

def shop_detail_view(request, id):
    product = Product.objects.get(id=id)
    product_list = Product.objects.all()[:5]
    return render(request, 'pages/shop-single.html', { 'product':product,'heading': 'Product Page', 'btn':True, 'product_list': product_list})

@login_required
def checkout(request, id):
    id = id
    return render(request, 'pages/checkout.html', {'heading': 'Checkout Page', 'id': id})

def charge(request, id):
    product = Product.objects.get(id=id)
    if request.method == 'POST':
        print(request.POST)
        customer = stripe.Customer.create(
                        email = request.POST['email'],
                        name = request.POST['nickname'],
                        source=request.POST['stripeToken'],
                    )   
        charge = stripe.Charge.create(
            customer=customer,
            amount = product.price*100,
            currency='inr',
            description='bootie payment'
        )
    return redirect(reverse('success'))

def successMsg(request):
    return render(request, 'pages/success.html', {'heading': 'Thankyou for shopping'})