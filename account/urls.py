# urls.py
from django.urls import path
from .views import signup, home, login_view, logout_view

urlpatterns = [
    path("", home, name="home"),
    path("signup/", signup, name="signup"),
    path("login/", login_view, name="login"),
    path("logout/", logout_view, name="logout"),
    # Add other URL patterns as needed
]
