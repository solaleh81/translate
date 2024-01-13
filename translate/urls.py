from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('service-1/', views.service1, name='service-1'),

]
