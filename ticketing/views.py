from django.http import HttpResponse
from django.shortcuts import render
from .models import BusRoute
from .filters import RouteFilter
def index(request):
    route_list=BusRoute.objects.all()
    myFilter = RouteFilter(request.GET, queryset=route_list )
    route_list = myFilter.qs
    context = {
        'route_list': route_list,
        'user': request.user,
        'myFilter': myFilter,
    }
    return render(request, 'ticketing/index.html', context)


def about(request):
    return render(request, 'ticketing/aboutus.html')