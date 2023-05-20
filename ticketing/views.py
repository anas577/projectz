from django.http import HttpResponse
from django.shortcuts import render
from .models import BusRoute

def index(request):
    objects = BusRoute.objects.all()
    return render(request,'index.html',{'objects':objects})


