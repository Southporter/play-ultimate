from django.contrib import admin

from .models import Game, GameDay, Sport

admin.site.register(Game)
admin.site.register(GameDay)
admin.site.register(Sport)
