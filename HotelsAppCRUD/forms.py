from django.forms import ModelForm
from django.forms.widgets import DateInput, TextInput

from .models import *


class HotelForm(ModelForm):
    class Meta:
        model = Hotel
        fields = ['name', 'description', 'star_rating', 'address1', 'address2', 'county', 'postal_code', 'country',
                  'latitude', 'longitude']


class CustomerForm(ModelForm):
    class Meta:
        model = Customer
        fields = ['name', 'credit_card_no', 'phone_number', 'email']
        widgets = {
            'credit_card_no': TextInput(attrs={'class': "input", 'placeholder': "0000-0000-0000-0000", 'data-mask': "####-####-####-####"}),
            'phone_number': TextInput(attrs={'class': "input", 'placeholder': "+999 99 999 9999", 'data-mask': "+###-##-###-####"}),
           }


class RoomForm(ModelForm):
    class Meta:
        model = Room
        fields = ['hotel_id', 'room_number', 'room_type', 'type', 'beds', 'max_occupancy', 'cost_per_night']


class RoomReservationForm(ModelForm):
    class Meta:
        model = RoomReservation
        fields = ['hotel_id', 'customer_id', 'room_id', 'reservation_description', 'from_date', 'to_date', 'number_of_adults',
                  'number_of_children', 'payment_no']
        widgets = {
          'from_date': DateInput(format='%m/%d/%Y', attrs={'class': "input", 'placeholder': "MM/dd/YYYY", 'data-mask': "##/##/####"}),
          'to_date':  DateInput(format='%m/%d/%Y', attrs={'class': "input", 'placeholder': "MM/dd/YYYY", 'data-mask': "##/##/####"}),
        }


class RoomServiceForm(ModelForm):
    class Meta:
        model = RoomService
        fields = ['service_description', 'service_price']


class RoomChargesForm(ModelForm):
    class Meta:
        model = RoomCharges
        fields = ['reservation_id', 'service_id', 'description', 'discount_code', 'discount_price']


class RoomBillingForm(ModelForm):
    class Meta:
        model = RoomBilling
        fields = ['customer_id', 'room_charge_id', 'invoice_no', 'billing_address1', 'billing_address2', 'county',
                  'postal_code', 'country', 'total_discounts', 'total_invoice']


class RoomReservationLookupForm(ModelForm):
    class Meta:
        model = RoomReservationView
        fields = ['hotel_id', 'customer_id', 'room_id', 'reservation_description', 'from_date', 'to_date', 'number_of_adults',
                  'number_of_children', 'payment_no']
