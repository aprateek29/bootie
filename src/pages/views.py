from django.shortcuts import render
from .models import Product

# Create your views here.
def index_view(request):
    product_list = Product.objects.all()
    return render(request, 'pages/index.html', {'product_list':product_list, 'heading': 'Casual Shoes for Men', 'trending': True, 'btn':True})

def about_view(request):
    return render(request, 'pages/about.html', { 'heading': 'About Us'})

def blog_view(request):
    return render(request, 'pages/blog.html', { 'heading': 'Blog Page'})

def contact_view(request):
    return render(request, 'pages/contact.html', { 'heading': 'Contact Us'})

def single_view(request):
    return render(request, 'pages/single.html', { 'heading': 'Blog'})

def shop_list_view(request):
    return render(request, 'pages/shop.html', { 'heading': 'Shop'})

def shop_detail_view(request, id):
    return render(request, 'pages/shop-single.html', { 'heading': 'Product Page', 'btn':True})