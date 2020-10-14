from cart import views
from django.urls import path, include
from django.contrib import admin
from cart.views import update, home_page, checkout
app_name = 'cart'
urlpatterns = [

    path('', home_page, name="home"),
    path('update/', update, name="update"),
    path('checkout/', checkout , name="checkout"),

]
