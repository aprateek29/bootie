from django.shortcuts import render

# Create your views here.
def index_view(request):
    return render(request, 'pages/index.html', {'product_list':[1,2,3,4]})