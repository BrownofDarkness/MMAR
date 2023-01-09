import django_filters
from .models import Client


class ClientFilterSearch(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='iexact')

    class Meta:
        model = Client
        fields = ['name']
