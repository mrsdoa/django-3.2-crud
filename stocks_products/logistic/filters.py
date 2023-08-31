from django_filters import rest_framework as filters

from .models import Stock


class StockFilter(filters.FilterSet):
    products_title = filters.CharFilter(field_name="products__title", lookup_expr='icontains')
    products_description = filters.CharFilter(field_name="products__description", lookup_expr='icontains')

    class Meta:
        model = Stock
        fields = ['products_title', 'products_description']