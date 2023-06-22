from django import forms
from .models import Ticket,Location,BusRoute,Bus

class TicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = ['first_name', 'last_name','cin']


