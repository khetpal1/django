from django.db import models
from catalogue.models import *

class Price(models.Model):
    service = models.ForeignKey(Service, on_delete=models.CASCADE, related_name='service_prices')
    starting_point = models.ForeignKey(ServiceStop, on_delete=models.CASCADE, related_name='starts')
    ending_point = models.ForeignKey(ServiceStop, on_delete=models.CASCADE, related_name='ends')

class DynamicPricing(models.Model):
    price = models.ForeignKey(Price, on_delete=models.CASCADE, related_name='dynamic_prices')
    booked_prior = models.IntegerField()
    effective_price = models.DecimalField(max_digits=6, decimal_places=2)

class CancellationPricing(models.Model):
    price = models.ForeignKey(Price, on_delete=models.CASCADE, related_name='cancellation_prices')
    cancelled_prior = models.IntegerField()
    charge = models.DecimalField(max_digits=6, decimal_places=2)