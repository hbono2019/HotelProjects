from django.db import models
from django.urls import reverse
from mongoengine import *

# Create your models here.
class Customer(models.Model):
    customer_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    credit_card_no = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=50, default='')
    email = models.CharField(max_length=100, default='')
    def get_absolute_url(self):
        return reverse('HotelsAppCRUD:customer_index')


class Hotel(models.Model):
    hotel_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=60)
    description = models.CharField(max_length=120)
    star_rating = models.IntegerField()
    address1 = models.CharField(max_length=120)
    address2 = models.CharField(max_length=120)
    county = models.CharField(max_length=120)
    postal_code = models.CharField(max_length=20)
    country =  models.CharField(max_length=120)
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)
    def get_absolute_url(self):
        return reverse('HotelsAppCRUD:hotel_index')


ROOM_TYPE = (
              ('D', 'Double Deluxe Room'),
              ('S', 'Single Deluxe Room'),
              ('H', 'Honey Moon Suite'),
              ('E', 'Economy Double'),
            )


TYPE_RESRV_ROOM = (
                    ('P', 'Package Deal'),
                    ('O', 'One Time Reservation'),
                    ('M', 'Membership Deal'),
                    ('C', 'Concierge Reservation'),
                   )


class Room(models.Model):
    room_id = models.AutoField(primary_key=True)
    hotel_id = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    room_number = models.IntegerField()
    room_type = models.CharField(max_length=60, choices=ROOM_TYPE, default='Economy Double')
    type = models.CharField(max_length=120, choices=TYPE_RESRV_ROOM, default='One Time Reservation')
    beds = models.IntegerField()
    max_occupancy = models.IntegerField()
    cost_per_night = models.IntegerField()
    def get_absolute_url(self):
        return reverse('HotelsAppCRUD:room_index')


class RoomReservation(models.Model):
    reservation_id = models.AutoField(primary_key=True)
    hotel_id = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    customer_id = models.ForeignKey(Customer, on_delete=models.CASCADE, default='')
    room_id = models.ForeignKey(Room, on_delete=models.CASCADE)
    room_number = models.CharField(max_length=120)
    from_date = models.DateField()
    to_date = models.DateField()
    number_of_adults = models.IntegerField()
    number_of_children = models.IntegerField()
    payment_no = models.CharField(max_length=120)
    def get_absolute_url(self):
        return reverse('HotelsAppCRUD:rooms_reservation_index')


class RoomService(models.Model):
    service_id = models.AutoField(primary_key=True)
    service_description = models.CharField(max_length=120)
    service_price = models.DecimalField(max_digits=5, decimal_places=2, default='')
    def get_absolute_url(self):
        return reverse('HotelsAppCRUD:rooms_service_index')


class RoomCharges(models.Model):
    room_charge_id = models.AutoField(primary_key=True)
    reservation_id = models.ForeignKey(RoomReservation, on_delete=models.CASCADE)
    service_id = models.ForeignKey(RoomService, on_delete=models.CASCADE)
    description = models.CharField(max_length=120, default='')
    discount_code = models.CharField(max_length=20, default='')
    discount_price = models.DecimalField(max_digits=5, decimal_places=2, default='')
    def get_absolute_url(self):
        return reverse('HotelsAppCRUD:rooms_charge_index')


class RoomBilling(models.Model):
    reservation_id = models.AutoField(primary_key=True)
    customer_id = models.ForeignKey(Customer, on_delete=models.CASCADE)
    room_charge_id = models.ForeignKey(RoomCharges, on_delete=models.CASCADE)
    invoice_no = models.CharField(max_length=120,default='')
    billing_address1 = models.CharField(max_length=120)
    billing_address2 = models.CharField(max_length=120)
    county =  models.CharField(max_length=120)
    postal_code = models.CharField(max_length=20)
    country =  models.CharField(max_length=120)
    total_discounts = models.DecimalField(max_digits=5, decimal_places=2,default='')
    total_invoice = models.DecimalField(max_digits=5, decimal_places=2,default='')
    def get_absolute_url(self):
        return reverse('HotelsAppCRUD:rooms_billing_index')
