from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('cart/', views.cart, name='cart'),
    path('employment/', views.cart, name='employment'),

]