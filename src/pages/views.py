from django.shortcuts import render
from .models import Product

# Create your views here.
def index_view(request):
    product_list = Product.objects.all()
    return render(request, 'pages/index.html', {'product_list':product_list})

def about_view(request):
    return render(request, 'pages/about.html', {})

def blog_view(request):
    return render(request, 'pages/blog.html', {})

def contact_view(request):
    return render(request, 'pages/contact.html', {})

def single_view(request):
    return render(request, 'pages/single.html', {})