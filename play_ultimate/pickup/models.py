from django.db import models
from django.conf import settings


class Game(models.Model):
    name = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    organizer = models.ForeignKey(settings.AUTH_USER_MODEL,
                                  on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class GameDay(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    attendees = models.ManyToManyField(settings.AUTH_USER_MODEL)

    def __str__(self):
        return 


