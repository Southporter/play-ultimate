from datetime import date
import calendar
from json import dumps
import subprocess

from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.forms import EmailField
from django.utils.translation import ugettext_lazy as _
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.core.exceptions import ObjectDoesNotExist
from django.core.serializers import serialize

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth import forms as auth_forms
from django.contrib.auth.models import User

from .models import GameDay


class UserCreationForm(auth_forms.UserCreationForm):
    email = EmailField(label=_("Email address"), required=True,
                       help_text=_("Required"))

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def save(self, commit=True):
        user = super(auth_forms.UserCreationForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user


def index(request):
    games = GameDay.objects.all()
    today = date.today()
    print("games: {0}".format(serialize('json', games)))
    day_name = calendar.day_name[today.weekday()]
    context = {'games': games, 'day': today.day, 'day_name': day_name}
    command_line_args = ['node', 'staticfiles/render.js', 'GamesView', dumps({
        'games': serialize('json', games), 'name': 'Game Day'
        })]
    process = subprocess.Popen(command_line_args, stdout=subprocess.PIPE)
    response = process.communicate()
    print('response: {0}'.format(response))
    html = response[0].decode('utf-8').strip()
    context['content'] = html
    return render(request, "pickup/main.html", context)


def detail(request, game_id):
    return HttpResponse("You are looking at game %s" % game_id)


@csrf_exempt
def attendee(request):
    try:
        print('request: {0}'.format(request))
        attendee_id = request.POST.get('attendee')
        game_id = request.POST.get('game')
        print(game_id)
        game_day = GameDay.objects.get(id__exact=game_id)
        print(game_day)
        game_day.attendees.add(attendee_id)
        return HttpResponse(status='201')
    except ObjectDoesNotExist:
        return HttpResponse(status='405')


def render_failed_login(request):
    context = {'error': True, 'is_login': True}
    return render(request, "pickup/login.html", context)


class Login(View):
    def get(self, request):
        context = {'is_login': True, 'is_signup': False}
        return render(request, "pickup/login.html", context)

    def post(self, request):
        form = auth_forms.AuthenticationForm(data=request.POST)
        if form.is_valid():
            clean_data = form.clean()
            username = clean_data['username']
            password = clean_data['password']
            user = authenticate(request, username=username, password=password)
            print(user)
            if user is not None:
                login(request, user)
                return redirect('games:index')
            else:
                return render_failed_login(request)
        else:
            return render_failed_login(request)


class Signup(View):
    def post(self, request):
        context = {'is_signup': True}
        form = UserCreationForm(request.POST)
        print("Form is valid? {0}".format(form.is_valid()))
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('games:index')
        context['signup_form'] = form
        print(form.username)
        return render(request, "pickup/login.html", context)

    def get(self, request):
        context = {'is_signup': True}
        form = UserCreationForm()
        context['signup_form'] = form
        return render(request, "pickup/login.html", context)


class Logout(View):
    def get(self, request):
        logout(request)
        return redirect('games:index')
