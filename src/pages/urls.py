from django.urls import path
from . import views

urlpatterns = [
    path('', views.index_view, name='index'),
    path('about/', views.about_view, name='about'),
    path('blog/', views.blog_view, name='blog'),
    path('contact/', views.contact_view, name='contact'),
    path('single/', views.single_view, name='single'),
    path('shop/', views.shop_list_view, name='shop'),
    path('shop/<id>', views.shop_detail_view, name='shop-detail'),
]