from orders.utils import unique_order_id_generator
from django.db import models
from cart.models import Create
from django.db.models.signals import pre_save, post_save
import math
from billing.models import BIllingProfile


# Create your models here.
ORDER_STATUS_CHOICES = (

    ('created', 'Created'),
    ('paid', 'Paid'),
    ('shipped', 'SHipped'),
    ('refunded', 'Refunded'),
)


class Order(models.Model):
    billlingprofile=models.ForeignKey( BIllingProfile, on_delete=models.PROTECT, null=True, blank=True)
    order_id = models.CharField(max_length=120, blank=True)
    Cart = models.ForeignKey(Create, on_delete=models.PROTECT)
    Status = models.CharField(
        max_length=120, default="created", choices=ORDER_STATUS_CHOICES)
    shipping_Total = models.DecimalField(
        default=5.05, max_digits=100, decimal_places=2)
    Total = models.DecimalField(default=0.00, max_digits=100, decimal_places=2)

    def __str__(self):
        return self.order_id

    def update_total(self):
        cart_total = self.Cart.Total
        shippingTotal = self.shipping_Total
        New_Total = math.fsum([ shippingTotal, cart_total])
        self.Total = New_Total
        print(New_Total)
        self.save()
        return New_Total


def pre_save_order_id_genrator(sender, instance, *args, **kwargs):

    instance.order_id = unique_order_id_generator(instance)


pre_save.connect(pre_save_order_id_genrator, sender=Order)


def post_save_Cart_orderid(sender, instance, created, *args, **kwargs):
    if not created:
        cart_obj = instance
        print(instance)
        print("instancesss")
        cart_total = cart_obj.Total
        print(cart_total)
        cart_id = cart_obj.id
        print(cart_id)
        print("whats this...")

        qs = Order.objects.filter(Cart__id=cart_id)
        for q in qs:
            print(q)
        print(qs)
        if qs.count() == 1:
            order_obj = qs.first()
            print(order_obj)
            print("what is it")
            order_obj.update_total()
post_save.connect(post_save_Cart_orderid, sender=Create)

def post_save_order(sender, instance, created, *args, **kwargs):
    if created:
        instance.update_total()

post_save.connect(post_save_order, sender=Order)


