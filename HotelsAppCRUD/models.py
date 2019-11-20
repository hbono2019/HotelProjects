from django.db import models
from django.urls import reverse
from mongoengine import *

# Create your models here.
class Customer(models.Model):
    customer_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    credit_card_no = models.CharField(max_length=100, blank=True, null=True)
    phone_number = models.CharField(max_length=50, default='')
    email = models.CharField(max_length=100, default='')
    def get_absolute_url(self):
        return reverse('HotelsAppCRUD:customer_index')

    def __str__(self):
        return "(%s) %s" % (self.customer_id, self.name)


class Hotel(models.Model):
    hotel_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=60)
    description = models.CharField(max_length=120)
    star_rating = models.IntegerField()
    address1 = models.CharField(max_length=120)
    address2 = models.CharField(max_length=120, blank=True, null=True)
    county = models.CharField(max_length=120)
    postal_code = models.CharField(max_length=20)
    country = models.CharField(max_length=120)
    latitude = models.DecimalField(max_digits=9, decimal_places=7)
    longitude = models.DecimalField(max_digits=9, decimal_places=7)
    def get_absolute_url(self):
        return reverse('HotelsAppCRUD:hotel_index')

    def __str__(self):
        return "(%s) %s" % (self.hotel_id, self.name)



class Room(models.Model):
    DOUBLE_DELX = 'D'
    SINGLE = 'S'
    HONEYMN = 'H'
    ECONOMY = 'E'
    ROOM_TYPE = (
        (DOUBLE_DELX, 'Double Deluxe Room'),
        (SINGLE, 'Single Deluxe Room'),
        (HONEYMN, 'Honey Moon Suite'),
        (ECONOMY, 'Economy Double'),
    )
    PACKAGE_DEAL = 'P'
    ONE_TIME_RSRV = 'O'
    MEMBERSHIP_DL = 'M'
    CONCIERGE_RSRV = 'C'
    TYPE_RESRV_ROOM = (
        (PACKAGE_DEAL, 'Package Deal'),
        (ONE_TIME_RSRV, 'One Time Reservation'),
        (MEMBERSHIP_DL, 'Membership Deal'),
        (CONCIERGE_RSRV, 'Concierge Reservation'),
    )
    room_id = models.AutoField(primary_key=True)
    hotel_id = models.ForeignKey(Hotel, on_delete=models.CASCADE, related_name='room_hotel')
    room_number = models.IntegerField()
    room_type = models.CharField(max_length=60, choices=ROOM_TYPE, default=ECONOMY)
    type = models.CharField(max_length=120, choices=TYPE_RESRV_ROOM, default=ONE_TIME_RSRV)
    beds = models.IntegerField()
    max_occupancy = models.IntegerField()
    cost_per_night = models.DecimalField(max_digits=6, decimal_places=2)
    def get_absolute_url(self):
        return reverse('HotelsAppCRUD:room_index')

    def __str__(self):
        return "(%s) %s" % (self.room_id, self.room_number)


class RoomReservation(models.Model):
    reservation_id = models.AutoField(primary_key=True)
    hotel_id = models.ForeignKey(Hotel, on_delete=models.CASCADE, related_name='reservation_hotel')
    customer_id = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='reservation_customer', default='')
    room_id = models.ForeignKey(Room, on_delete=models.CASCADE, related_name='reservation_room')
    reservation_description = models.CharField(max_length=60, default='')
    from_date = models.DateField()
    to_date = models.DateField()
    number_of_adults = models.IntegerField()
    number_of_children = models.IntegerField()
    payment_no = models.CharField(max_length=120, blank=True, null=True)
    def get_absolute_url(self):
        return reverse('HotelsAppCRUD:rooms_reservation_index')

    def __str__(self):
        return "(%s) %s (%s) (%s)" % (self.reservation_id, self.reservation_description, self.from_date, self.to_date)



class RoomService(models.Model):
    service_id = models.AutoField(primary_key=True)
    service_description = models.CharField(max_length=120)
    service_price = models.DecimalField(max_digits=5, decimal_places=2, default='')
    def get_absolute_url(self):
        return reverse('HotelsAppCRUD:rooms_service_index')

    def __str__(self):
        return "(%s) %s" % (self.service_id, self.service_description)


class RoomCharges(models.Model):
    room_charge_id = models.AutoField(primary_key=True)
    reservation_id = models.ForeignKey(RoomReservation, on_delete=models.CASCADE, related_name='charge_reservation')
    service_id = models.ForeignKey(RoomService, on_delete=models.CASCADE,related_name='charge_service')
    description = models.CharField(max_length=120, default='')
    discount_code = models.CharField(max_length=20, default='', blank=True, null=True)
    discount_price = models.DecimalField(max_digits=5, decimal_places=2, default='')
    def get_absolute_url(self):
        return reverse('HotelsAppCRUD:rooms_charge_index')

    def __str__(self):
        return "(%s) %s" % (self.room_charge_id, self.description)


class RoomBilling(models.Model):
    reservation_id = models.AutoField(primary_key=True)
    customer_id = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='billing_customer')
    room_charge_id = models.ForeignKey(RoomCharges, on_delete=models.CASCADE, related_name='billing_charge')
    invoice_no = models.CharField(max_length=120, default='')
    billing_address1 = models.CharField(max_length=120)
    billing_address2 = models.CharField(max_length=120, blank=True, null=True)
    county = models.CharField(max_length=120)
    postal_code = models.CharField(max_length=20)
    country = models.CharField(max_length=120)
    total_discounts = models.DecimalField(max_digits=5, decimal_places=2, default='')
    total_invoice = models.DecimalField(max_digits=5, decimal_places=2, default='')
    def get_absolute_url(self):
        return reverse('HotelsAppCRUD:rooms_billing_index')

    def __str__(self):
        return "(%s) %s" % (self.reservation_id, self.invoice_no)

