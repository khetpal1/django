from django.urls import path
from .views import *

app_name = 'people'



urlpatterns = [

    path('', HomeView.as_view(), name='Home'),
    path('category/', CategoryView.as_view(), name='Category'),
    path('detail/', DetailView.as_view(),name='Detail'),
    path('register/', CustomerView.as_view(), name='register'),
    
   
        

]	