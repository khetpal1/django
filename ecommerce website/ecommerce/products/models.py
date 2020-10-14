from django.db import models
import random
import os
from products.utility import unique_slug_generator
from django.db.models.signals import pre_save
from django.urls import reverse


def get_filename_ext(filename):
    base_name = os.path.basename(filename)
    name, ext = os.path.splitext(base_name)
    return name, ext


def uplaod_path_file(instance, filename):
    print(instance)
    print(filename)
    new_filename = random.randint(2, 358974656245)
    name, ext = get_filename_ext(filename)
    return f"Products/{new_filename}.{ext}"


class ProductManager(models.Manager):
    def featured(self):
        return self.get_queryset().filter(featured=True)

    def get_by_id(self, id):
        return self.get_queryset().filter(id=id)

    def search(self, query):
        return self.get_queryset().search(query)


class Products(models.Model):

    title = models.CharField(max_length=50)
    description = models.TextField()
    slug = models.SlugField(blank=True, unique=True)
    price = models.DecimalField(decimal_places=2, max_digits=20)
    image = models.ImageField(
        upload_to="ecommerce\products\productimage", null=True, blank=True)
    featured = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True)

    def get_absolute_url(self):
        return"/products/{slug}/".format(slug=self.slug)
        # return reverse("products": "article", kwargs={"slug": self.slug})

    objects = ProductManager()

    def __str__(self):
        return self.title


def product_pre_save_reciever(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)


pre_save.connect(product_pre_save_reciever, sender=Products)
