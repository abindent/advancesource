from django.urls import path
from . import views
urlpatterns = [
    # Auth 
     # Sign Up
    path('signup', views.handleSignUp, name="Signup"),

    #Login
    path('login', views.handeLogin, name="Login"),

    # Logout
    path('logout', views.handlelogout, name="Logout"),
]