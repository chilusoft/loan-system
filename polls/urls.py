from django.urls import path

from . import views



urlpatterns = [
    path('', views.index, name='index'),
    path('customers', views.customers, name='customers'),
   # path('customer/<int:customer_id>/', views.customers, name='customer')
]
