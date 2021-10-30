from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Game(models.Model):
    room_code = models.CharField(max_length=100)
    creator_of_the_game = models.CharField(max_length=100)
    game_opponent = models.CharField(max_length=100, blank= True, null= True)
    is_over = models.BooleanField(default=False)