from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.login2,name="login2"),
    path('home/',views.home,name="home"),
    path('home/index.html',views.index,name="index"),
    path('save_order/', views.save_order, name='save_order'),  
    path("home/filter_orders.html", views.filter_orders, name="filter_orders"),
    path('home/vendors.html',views.vendors,name="vendors"),
    path("save_vendor/", views.save_vendor, name="save_vendor"),
    path('filter_orders/',views.filter_orders,name="filter_orders"),
    path('registration/',views.registration,name="registration"),
    path('home/login2.html',views.login2,name="login"),
    path('home/dashboard.html', views.dashboard, name='dashboard'),
    path('delete_vendor/<int:vendor_id>/', views.delete_vendor, name='delete_vendor'),
    path('update_payment_status/<int:vendor_id>/', views.update_payment_status, name='update_payment_status'),
]
