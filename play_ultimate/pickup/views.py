from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout


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
        print('username: {0}'.format(username))
        print('password: {0}'.format(password))
        user = authenticate(request, username=username, password=password)
        print(user)
        if user is not None:
            login(request, user)
            return redirect('games:index')
        else:
            context = {'error': True, 'is_login': True}
            return render(request, "pickup/login.html", context)
    else:
        context = {'is_login': True, 'is_signup': False}
        return render(request, "pickup/login.html", context)


def signup_request(request):
    context = {'is_signup': True}
    return render(request, "pickup/login.html", context)


def logout_request(request):
    logout(request)
    return redirect('games:index')
