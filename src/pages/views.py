from django.shortcuts import render, redirect
from .models import Product, Contact, Newsletter
from django.contrib import messages
from .filters import ProductFilter
from django.contrib.auth.decorators import login_required

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
    product_list = Product.objects.all()[:5]
    filter = ProductFilter(request.GET, queryset=Product.objects.all())
    print(filter)
    return render(request, 'pages/shop.html', {'filter': filter, 'heading':'Shop', 'product_list': product_list})
    # return render(request, 'pages/shop.html', {'heading': 'Shop'})

def shop_detail_view(request, id):
    product = Product.objects.get(id=id)
    product_list = Product.objects.all()[:5]
    return render(request, 'pages/shop-single.html', { 'product':product,'heading': 'Product Page', 'btn':True, 'product_list': product_list})

@login_required
def checkout(request):
    if request.user.is_anonymous:
        messages.success(request, 'You have to login first')


    return render(request, 'pages/checkout.html', {})