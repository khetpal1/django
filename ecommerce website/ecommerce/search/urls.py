from django.conf.urls import url
from django.urls import path
from . import views

from .views import Searchproduct_listview
app_name = 'search'

urlpatterns = [
    path('', Searchproduct_listview, name='query'),
]
