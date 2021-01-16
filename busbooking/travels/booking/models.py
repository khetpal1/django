from django.db.models.aggregates import Max
from people.models import Customer
from django.db import models
from catalogue.models import *
from price_availability.models import *
# Create your models here.

class BookingService(models.Model):
    service = models.ForeignKey(Service, on_delete=models.CASCADE, related_name='booking_services')
    date = models.DateField()
    is_cancelled = models.BooleanField(default=False)
    bus = models.ForeignKey(Bus, on_delete=models.SET_NULL, null=True, blank=True, related_name='runs')

class Booking(models.Model):
    booking_service = models.ForeignKey(BookingService, on_delete=models.CASCADE, related_name='bookings')
    customer = models.OneToOneField(Customer, on_delete=models.CASCADE, related_name='customer')
    is_cancelled = models.BooleanField(default=False)

class Passenger(models.Model):
    booking = models.ForeignKey(Booking, on_delete=models.CASCADE, related_name='passengers')
    name = models.CharField(max_length=127)
    #gender = 
    #age

class BookingCost(models.Model):
    booking = models.ForeignKey(Booking, on_delete=models.CASCADE, related_name='booking_costs')
    price = models.ForeignKey(Price, on_delete=models.CASCADE, related_name='price_costs')

#Expand on this as availability can be stop to stop
class Availability(models.Model):
    service = models.ForeignKey(BookingService, on_delete=models.CASCADE, related_name='booking_service_availability')
