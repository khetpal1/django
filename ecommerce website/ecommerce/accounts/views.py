from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import  Loginform, Registerform, guest_form
from django.contrib.auth import authenticate, login, get_user_model
from .models import Guest_Email

# Create your views here.
def gues_login_form(request):
    if request.method=="POST":
        form = guest_form(request.POST or None)
        if form.is_valid():
            email = form.cleaned_data.get("email")
            print(email)
            new_guest_email= Guest_Email.objects.create(email=email)
            request.session['guest_email_id']=new_guest_email.id
            return redirect("/cart/checkout/")
        return redirect("/register/")
def loginpage(request):
    form = Loginform(request.POST or None)
    context = {
        "form": form
    }
    if form.is_valid():
        print(form.cleaned_data)
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            context[form] = Loginform()
            return redirect("/")
        else:
            # Return an 'invalid login' error message.
            print("error")
    return render(request, "accounts/loginpage.html", context)
User = get_user_model()


def register(request):
    form = Registerform(request.POST or None)
    context = {
        "form": form
    }
    if form.is_valid():
        username = form.cleaned_data.get("username")
        email = form.cleaned_data.get("email")
        password = form.cleaned_data.get("password")

        newuser = User.objects.create_user(username, email, password)
        print(newuser)
        print(form.cleaned_data)
    return render(request, "accounts/register.html", context)
