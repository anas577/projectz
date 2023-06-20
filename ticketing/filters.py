import django_filters
from django_filters import DateFilter
from .models import BusRoute



class RouteFilter(django_filters.FilterSet):
    date = DateFilter(field_name="departure_time",lookup_expr='gte', label='Date')
    start_point = django_filters.CharFilter(lookup_expr='icontains', label='From')
    destination = django_filters.CharFilter(lookup_expr='icontains', label='To')
    class Meta:
        model = BusRoute
        fields = '__all__'
        exclude = ['arrival_time', 'price', 'departure_time', 'bus']
