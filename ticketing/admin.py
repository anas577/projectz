from django.contrib import admin

# Register your models here.

from .models import  Bus, BusRoute, Ticket, Location

admin.site.register(Bus)
admin.site.register(BusRoute)
admin.site.register(Ticket)
admin.site.register(Location)
