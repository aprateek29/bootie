import django_filters
from .models import Product

class ProductFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='icontains')
    rating = django_filters.NumberFilter(field_name='rating', lookup_expr='lte')
    price = django_filters.NumberFilter(field_name='price', lookup_expr='lte')
    # tags = django_filters.CharFilter(lookup_expr='iexact')


    class Meta:
        model = Product
        fields = []

