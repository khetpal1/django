from django.db import models

# Create your models here.
from products.models import Products
from django.conf import settings

from django.db.models.signals import pre_save, post_save, m2m_changed

User = settings.AUTH_USER_MODEL


class new_get(models.Manager):

    def new_or_get(self, request):
        cart_id = request.session.get("cart_id", None)
        qs = Create.objects.filter(id=cart_id)
        if qs.count() == 1:
            print("exist")
            cart_obj = qs.first()
            if request.user.is_authenticated:
                cart_obj.user = request.user
                cart_obj.save()
        else:
            cart_obj = Create.objects.new(user=request.user)
            request.session["cart_id"] = cart_obj.id

        return cart_obj

    def new(self, user=None):
        user_obj = None
        if user is not None:
            if user.is_authenticated:
                user_obj = user
        return self.model.objects.create(user=user_obj)


class Create(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.PROTECT, null=True, blank=True)
    products = models.ManyToManyField(Products, blank=True)
    Total = models.DecimalField(default=0.00, max_digits=100, decimal_places=2)
    updated = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    objects = new_get()

    def __str__(self):
        return str(self.id)


def pre_save_total(sender, instance, action, *args, **kwargs):
    products = instance.products.all()
    Total = 0
    for x in products:
        Total += x.price
    instance.Total = Total
    instance.save()


m2m_changed.connect(pre_save_total, sender=Create.products.through)
