from django.db import models
from django.contrib.auth.models import User
# Create your models here.




class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=20)

class Driver(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=20)

class TravelAgent(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=20)



class Address(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='addresses')
    line1 = models.CharField(max_length=127)
    line2 = models.CharField(max_length=127, null=True, blank=True)
    line3 = models.CharField(max_length=127, null=True, blank=True)
    city = models.CharField(max_length=31)
    state = models.CharField(max_length=31)
    pincode = models.CharField(max_length=15)