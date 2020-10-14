from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from products.views import product_listview, product_view, product_detialedview, article_detail, product_detaillistview, productfeaturedetailview, productfeaturelistview
from .import views

app_name = 'products'

urlpatterns = [

    path('', views.product_listview, name='listview'),
    # path('detail/<int:pk>/', product_detialedview.as_view(), name="detail"),
    path('<slug:slug>/', article_detail.as_view(), name='article'),

    path('detailfbv/<int:pk>/', product_detaillistview, name="detailproduct"),
    path('featuredetail/<int:pk>/',
         productfeaturedetailview.as_view(), name="detailproduct"),
    path('featurelist/<int:pk>/',
         productfeaturelistview.as_view(), name="detailproduct"),
]
