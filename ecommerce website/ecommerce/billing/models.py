from django.db import models
from django.conf import settings
from django.db.models.signals import post_save

# Create your models here.
User=settings.AUTH_USER_MODEL


class BIllingProfile(models.Model):
    user= models.OneToOneField(User, unique=True, on_delete=models.PROTECT, null=True, blank=True)
    email=models.EmailField()
    update=models.DateTimeField(auto_now_add=True)
    active =models.BooleanField(default=True)
    timestamp=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.email


def user_created_reciever(sender, instance, created, *args, **kwargs):
    if created:
        BIllingProfile.objects.get_or_create(user=instance, email=instance.email)
        print(BIllingProfile.objects)
        print("bliiinininih..............")

post_save.connect(user_created_reciever, sender=User)