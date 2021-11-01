from django.urls import path 
from .views import *

urlpatterns = [
    path("", index, name="index"),

    path("about", about, name="About"),
    
    path('games', game, name="game"),

    path('contact', contact, name="Contact")
]