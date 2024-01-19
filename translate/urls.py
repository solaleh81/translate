from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('service-1/', views.service1, name='service-1'),
    path('success/', views.success, name='success'),
    path('create_order/', views.create_order, name='create_order'),

]
