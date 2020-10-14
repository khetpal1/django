"""ecommerce URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from products.views import product_view, product_detialedview, article_detail, product_detaillistview
from ecommerce.views import home_page, aboutus, contact
from accounts.views import loginpage, register, gues_login_form
from django.views.generic import TemplateView
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_page, name='home'),
    path('aboutus/', aboutus, name="aboutus"),
    path('contact/', contact, name="contact"),
    path('loginpage/', loginpage, name="loginpage"),
    path('register/guest', gues_login_form, name="gues_login"),
    path('logout/', LogoutView.as_view(), name="logout"),
    path('register/', register, name="register"),
    path('bootstrap/', TemplateView.as_view(template_name="bootstrap/example.html"), name='bootstrap'),
    path('products/', include("products.urls", namespace="products")),
    path('search/', include("search.urls", namespace="search")),
    path('cart/', include("cart.urls", namespace="cart")),


]

if settings.DEBUG:
    urlpatterns = urlpatterns + \
        static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns = urlpatterns + \
        static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
