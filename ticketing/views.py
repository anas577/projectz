from django.db.models import Max
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import BusRoute, Ticket
from .filters import RouteFilter
from .forms import TicketForm
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

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

def book(request,routeid):
    print(request.user.id)
    if not request.user.is_authenticated:
        return redirect('loggin')
    if request.method == 'POST':
        form = TicketForm(request.POST)
        if form.is_valid():
            ticket = form.save(commit=False)
            ticket.user_id = request.user.id
            ticket.bus_route_id = routeid
            ticket.save()
            return ticket.generate_pdf()
    else:
        bus_route_id = request.GET.get('route_id')
        initial_data = {
            'user': request.user.id,
            'bus_route_id': routeid,
        }
        form = TicketForm(initial=initial_data)
    return render(request, 'ticketing/book.html', {'form': form})

def tracking(request):
    return render(request, 'ticketing/tracking.html')