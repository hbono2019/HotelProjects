import datetime

from django.core.exceptions import ValidationError
from django.forms import ModelForm
from django.utils.translation import ugettext_lazy as _

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


class RoomForm(ModelForm):
    class Meta:
        model = Room
        fields = ['hotel_id', 'room_number', 'room_type', 'type', 'beds', 'max_occupancy', 'cost_per_night']


class RoomReservationForm(ModelForm):
    def clean_from_date(self):
        from_date_data = self.cleaned_data['from_date']

        # Check if a date is not in the past.
        if from_date_data < datetime.date.today():
            raise ValidationError(_('Invalid date - cannot do reservations in the past'))
        # Check if a date is in the allowed range (+24 weeks from today).
        if from_date_data > datetime.date.today() + datetime.timedelta(weeks=24):
            raise ValidationError(_('Invalid date - reservations cannot be more than 24 weeks ahead'))
        # Remember to always return the cleaned data.
        return from_date_data

    def clean_to_date(self):
        to_date_data = self.cleaned_data['to_date']
        # Check if a date is not in the past.
        if to_date_data < datetime.date.today():
            raise ValidationError(_('Invalid date - cannot do reservations in the past'))
        # Check if a date is in the allowed range (+24 weeks from today).
        if to_date_data > datetime.date.today() + datetime.timedelta(weeks=24):
            raise ValidationError(_('Invalid date - reservations cannot be more than 24 weeks ahead'))
        # Remember to always return the cleaned data.
        return to_date_data

    class Meta:
        model = RoomReservation
        fields = ['hotel_id', 'customer_id', 'room_id', 'room_number', 'from_date', 'to_date', 'number_of_adults',
                  'number_of_children', 'payment_no']


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
