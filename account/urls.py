# urls.py
from django.urls import path
from .views import signup, home

urlpatterns = [
    path('', home, name='home'),
    path('signup/', signup, name='signup'),
    # Add other URL patterns as needed
]
