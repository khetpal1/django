from __future__ import unicode_literals
from django.contrib import admin
from .models import Products


# Register your models here.

class adminmodel(admin.ModelAdmin):
    list_display = [
        "title", "description", "id"
    ]

    list_filter = ("title", "description", "id"
                   )
    list_display = ["__str__", "slug"]

    class Meta:
        model = Products


admin.site.register(Products, adminmodel)
