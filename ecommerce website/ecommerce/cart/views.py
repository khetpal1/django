from django.shortcuts import render, redirect
from products.models import Products
from billing.models import BIllingProfile
# Create your views here.
from accounts.models import Guest_Email
from .models import Create
from accounts.forms import Loginform, guest_form
from orders.models import Order
# cart_id = request.session.get("cart_id", None)
# qs = Create.objects.filter(id=cart_id)
# if qs.count() == 1:
#     print("exist")
#     cart_obj = qs.first()
#     if request.user.is_authenticated:
#         cart_obj.user = request.user
#         cart_obj.save()
# else:
#     cart_obj = Create.objects.new(user=request.user)
#     request.session["cart_id"] = cart_obj.id

# return render(request, "carts/cart.html", {})
def home_page(request):
    cart_obj = Create.objects.new_or_get(request)

    return render(request, "carts/cart.html", {"cart": cart_obj})
    
def update(request):
    print(request.POST)
    print("whats post")
    id = request.POST.get("product")
    print(id)
    obj = Products.objects.get(id=id)
    cart_obj = Create.objects.new_or_get(request)
    if obj in cart_obj.products.all():
        cart_obj.products.remove(obj)
    else:
        cart_obj.products.add(obj)

    return redirect("cart:home")

def checkout(request):
    # order_obj=Order.objects.all()
    cart_obj= Create.objects.new_or_get(request)
    order_obj = None
    if cart_obj.products.count() == 0:
        return redirect("cart:home")  
    print(order_obj)
    print("helloooo...")
    # for i in order_obj:
    user=request.user
    login_form=Loginform()
    # guest_form= guest_form()
    guest_email_id=request.session.get('guest_email_id')
    # billing_profile=None
    # if user.is_authenticated:
    #     billing_profile=BIllingProfile.objects.get_or_create(user=user, email=user.email)
    # elif guest_email_id is not None:
    #     gues_email_obj=Guest_Email.objects.get(id=guest_email_id)
    #     billing_profile=BIllingProfile.objects.get_or_create(email=gues_email_obj.email)
    # else:
    #     pass
    # if billing_profile is not None:
    #     order_qs=Order.objects.filter(billling_profile=billing_profile, cart=cart_obj)
    #     if order_qs.count()==1:
    #         order_obj=order_qs.first()
    #     else:
    #         older_qs= Order.objects.exclude(billlingprofile=billing_profile, cart=cart_obj)
    #         order_obj=Order.objects.create(billlingprofile=billing_profile, cart=cart_obj)

    
    context = {"i": order_obj,
    # "billing_profile": billing_profile,
    "login_form": Loginform,
    "guest_email":guest_form()}
    
    # # else:
    # order_obj= Order.objects.get_or_create(Cart=cart_obj)
    return render(request, 'carts/checkout.html', context)