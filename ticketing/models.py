from django.db import models
from django.contrib.auth.models import User


class Bus(models.Model):
    #(value, display_name)
    STATUS_CHOICES = (
        ('confort', 'Confort'),
        ('premium', 'Premium'),
    )
    number = models.CharField(max_length=50)
    capacity = models.IntegerField()
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


class Ticket(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    bus_route = models.ForeignKey(BusRoute, on_delete=models.CASCADE)
    seat_number = models.IntegerField(default=1)




class Location(models.Model):
    latitude = models.FloatField()
    longitude = models.FloatField()
    timestamp = models.DateTimeField(auto_now_add=True)
    bus = models.ForeignKey(Bus, on_delete=models.CASCADE)

