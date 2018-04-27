from django.urls import path

from . import views

app_name = 'games'
urlpatterns = [
    path('', views.index, name='index'),
    path('login', views.login_request, name="Login"),
    path('game/<int:game_id>', views.detail, name='Game Detail'),
    path('account', views.detail, name="account"),
]
