from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.register, name='register'),
    path('products_list/', views.products_list, name='product_list'),
    path('admin_login/', views.admin_login, name='admin_login'),
    path('sign_in/', views.sign_in, name='sign_in'),
    path('search/', views.search_results, name='search_results'),
    path('changecart/', views.changecart, name='addcart'),
    path('resetcart/', views.resetcart, name='resetcart'),
    path('admin_in/', views.admin_in, name='admin_in'),
    #path('getOrder/',getOrder, name='admin'),
    path('getdata/',views.getdata),
    path('logout/',views.logout, name='logout'),
    path('detail/',views.detail, name='detail'),
    path('chufa/',views.admindetail, name='chufa'),
    path('createOrder/',views.createOrder, name='createOrder'),
]