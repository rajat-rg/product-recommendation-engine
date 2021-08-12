from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="Home"),
    path('signup', views.handleSignup, name="Signup"),
    path('login', views.handleLogin, name="Login"),
]
