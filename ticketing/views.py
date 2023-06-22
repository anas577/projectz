from django.shortcuts import render, redirect
from .models import BusRoute, Ticket, Location
from .filters import RouteFilter
from .forms import TicketForm
import json


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


def bus_location(request):
    if request.method == 'POST':
        tracking_code = request.POST.get('tracking_code')

        # Retrieve the bus locations from the JSON file
        bus_locations = Location.get_locations_from_json(tracking_code)

        # Prepare the bus location data for the OpenStreetMap API
        markers = []
        for location in bus_locations:
            markers.append({
                'lat': location['latitude'],
                'lon': location['longitude'],
                'popup': location['timestamp'].strftime('%Y-%m-%d %H:%M:%S')
            })

        # Pass the bus locations and map data to the template
        context = {
            'bus_locations': bus_locations,
            'markers': json.dumps(markers),
        }

        return render(request, 'ticketing/bus_location.html', context)

    return render(request, 'ticketing/bus_location.html')