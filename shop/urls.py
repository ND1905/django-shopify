from django.contrib import admin
from django.urls import path
from . import views
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index,name="ShopHome"),
    path('about/', views.about,name="AboutUs"),
    path('contact/', views.contact,name="ContactUs"),
    path('tracker/', views.tracker,name="TrackStatus"),
    path('search/', views.search,name="Search"),
    path('productview/<int:myid>/', views.productView,name="productView"),
    path('checkout/', views.checkout,name="Checkout"),
]