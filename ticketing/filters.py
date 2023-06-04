import django_filters
from django_filters import DateFilter
from .models import BusRoute

class RouteFilter(django_filters.FilterSet):
    date = DateFilter(field_name="departure_time",lookup_expr='gte')
    class Meta:
        model = BusRoute
        fields = '__all__'
        exclude = ['arrival_time', 'price','departure_time']
