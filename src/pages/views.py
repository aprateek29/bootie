from django.shortcuts import render

# Create your views here.
def index_view(request):
    return render(request, 'pages/index.html', {'product_list':[1,2,3,4]})

def about_view(request):
    return render(request, 'pages/about.html', {})

def blog_view(request):
    return render(request, 'pages/blog.html', {})

def contact_view(request):
    return render(request, 'pages/contact.html', {})