from django.db import models


# Create your models here.
class Customer(models.Model):
    customer_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    credit_card_no =  models.CharField(max_length=100)

class Hotel(models.Model):
    hotel_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=60)
    description = models.CharField(max_length=120)
    star_rating = models.IntegerField()
    address = models.CharField(max_length=120)
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)


class Room(models.Model):
    room_id = models.AutoField(primary_key=True)
    hotel_id = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    room_number = models.IntegerField()
    room_type = models.CharField(max_length=60)
    type = models.CharField(max_length=120)
    beds = models.IntegerField()
    max_occupancy = models.IntegerField()
    cost_per_night = models.IntegerField()


class RoomReservation(models.Model):
    reservation_id = models.AutoField(primary_key=True)
    hotel_id = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    customer_id = models.ForeignKey(Customer, on_delete=models.CASCADE,default='')
    room_id = models.ForeignKey(Room, on_delete=models.CASCADE)
    room_number = models.CharField(max_length=120)
    from_date = models.DateTimeField()
    to_date = models.DateTimeField()

class RoomService(models.Model):
    service_id = models.AutoField(primary_key=True)
    service_description = models.CharField(max_length=120)
    service_price = models.DecimalField(max_digits=5, decimal_places=2)

class RoomCharges(models.Model):
    room_charge_id = models.AutoField(primary_key=True)
    reservation_id = models.ForeignKey(RoomReservation, on_delete=models.CASCADE)
    service_id = models.ForeignKey(RoomService, on_delete=models.CASCADE)

class RoomBilling(models.Model):
    reservation_id = models.AutoField(primary_key=True)
    customer_id = models.ForeignKey(Customer, on_delete=models.CASCADE)
    room_charge_id = models.ForeignKey(RoomCharges, on_delete=models.CASCADE)
    billing_address1 = models.CharField(max_length=120)
    billing_address2 = models.CharField(max_length=120)
    county =  models.CharField(max_length=120)
    postal_code = models.CharField(max_length=20)
    country =  models.CharField(max_length=120)
    total_invoice = models.DecimalField(max_digits=5, decimal_places=2)
