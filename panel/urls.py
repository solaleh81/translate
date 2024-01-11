from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('cart/', views.cart, name='cart'),
    path('employment/', views.employment, name='employment'),
    path('orders/', views.orders_transactions, name='orders'),
    path('ticket/', views.ticket, name='ticket'),
    path('wallet/', views.wallet, name='wallet'),

]