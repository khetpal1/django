from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import Contactform
from django.contrib.auth import authenticate, login, get_user_model


def home_page(request):
    return render(request, "home.html", {})


def aboutus(request):
    return render(request, "home.html", {})


def contact(request):
    contact_form = Contactform(request.POST or None)
    context = {
        "form": contact_form,
        "brand": "Ecommerce"
    }
    if contact_form.is_valid():
        print(contact_form.cleaned_data)
    if request.method == "POST":
        print(request.POST)
        print(request.POST.get)
        print(request.POST)
    return render(request, "contact.html", context)

