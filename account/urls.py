# urls.py
from django.urls import path
from .views import signup, home, login_view

urlpatterns = [
    path('', home, name='home'),
    path('signup/', signup, name='signup'),
    path('login/', login_view, name='login'),
    # Add other URL patterns as needed
]
