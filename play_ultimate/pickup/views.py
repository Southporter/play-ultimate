from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login


def index(request):
    context = {}
    return render(request, "pickup/index.html", context)


def detail(request, game_id):
    return HttpResponse("You are looking at game %s" % game_id)


def login_request(request):
    print("login request")
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        print('username: {0}').format(username)
        print('password: {0}').format(password)
        user = authenticate(username, password)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            context = {'error': True}
            return render(request, "pickup/login.html", context)
    else:
        return render(request, "pickup/login.html", context)
