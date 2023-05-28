from django.http import HttpResponse
from django.shortcuts import render
from .models import BusRoute

def index(request):
    route_list=BusRoute.objects.all()
    context = {
        'route_list': route_list,
        'user': request.user,
    }
    return render(request, 'ticketing/index.html', context)


