from django.db import models

# Create your models here.
class Guest_Email(models.Model):
  email=models.EmailField()
  active=models.BooleanField(default=True)
  update=models.BooleanField(default=True)
  timestamp=models.DateTimeField(auto_now_add=True)

  def __str__(self):
    return self.email