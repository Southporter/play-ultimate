from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    context = {}
    return render(request, "pickup/index.html", context)


def detail(request, game_id):
    return HttpResponse("You are looking at game %s" % game_id)
