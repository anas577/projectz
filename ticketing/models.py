from django.db import models
from django.contrib.auth.models import User
from django.db.models import Max
from django.http import HttpResponse
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas


class Bus(models.Model):
    #(value, display_name)
    STATUS_CHOICES = (
        ('confort', 'Confort'),
        ('premium', 'Premium'),
    )
    number = models.CharField(max_length=50)
    capacity = models.IntegerField(default=50)
    driver_name = models.CharField(max_length=100)
    type = models.CharField(max_length=20,choices=STATUS_CHOICES)



class BusRoute(models.Model):
    start_point = models.CharField(max_length=100)
    destination = models.CharField(max_length=100)
    departure_time = models.DateTimeField()
    arrival_time = models.DateTimeField()
    def duration(self):
        return self.arrival_time-self.departure_time
    bus = models.ForeignKey(Bus, on_delete=models.CASCADE)
    price = models.FloatField(default=0.0)

    def available_seats(self):
        total_capacity = self.bus.capacity  # Assuming 'capacity' is a field on the 'Bus' model
        sold_tickets_count = Ticket.objects.filter(bus_route=self).count()
        return total_capacity - sold_tickets_count


class Ticket(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    bus_route = models.ForeignKey(BusRoute, on_delete=models.CASCADE)
    seat_number = models.IntegerField(default=1, )
    first_name = models.CharField(max_length=30, default="")
    last_name = models.CharField(max_length=30, default="")
    cin = models.CharField(max_length=10, default="")

    def save(self, *args, **kwargs):
        if not self.pk:  # Only generate the PDF when creating a new ticket
            # Increment seat_number for the specific bus route and save the ticket
            max_seat_number = Ticket.objects.filter(bus_route=self.bus_route).aggregate(Max('seat_number'))[
                'seat_number__max']
            if max_seat_number is None:
                self.seat_number = 1
            elif max_seat_number < self.bus_route.bus.capacity - 1:
                self.seat_number = max_seat_number + 1
            else:
                raise ValueError("Maximum seat limit reached.")

            super().save(*args, **kwargs)

            # Generate the PDF
            self.generate_pdf()

    def generate_pdf(self):
        # Create a new PDF document
        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = f'attachment; filename=ticket_{self.id}.pdf'

        p = canvas.Canvas(response, pagesize=letter)

        # Customize the PDF content
        p.drawString(100, 750, 'Ticket Details')
        p.drawString(100, 700, f'Ticket ID: {self.id}')
        p.drawString(100, 650, f'First name: {self.first_name}')
        p.drawString(100, 600, f'Last name: {self.last_name}')
        p.drawString(100, 550, f'Bus Route: {self.bus_route.start_point} - {self.bus_route.destination}')
        p.drawString(100, 500, f'Seat Number: {self.seat_number}')

        # Add more fields as needed

        # Save the PDF document
        p.showPage()
        p.save()

        return response

class Location(models.Model):
    latitude = models.FloatField()
    longitude = models.FloatField()
    timestamp = models.DateTimeField(auto_now_add=True)
    bus = models.ForeignKey(Bus, on_delete=models.CASCADE)

