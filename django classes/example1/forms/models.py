from django.db import models

# Create your models here.


class products(models.Model):
    name = models.CharField(max_length=120)
    description = models.CharField(max_length=120)
    email = models.EmailField()

    def __str__(self):
        return self.name
