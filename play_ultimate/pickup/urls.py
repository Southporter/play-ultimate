from django.urls import path

from . import views

app_name = 'games'
urlpatterns = [
    path('', views.index, name='index'),
    path('login', views.login_request, name="login"),
    path('signup', views.signup_request, name="signup"),
    path('logout', views.logout_request, name="logout"),
    path('game/<int:game_id>', views.detail, name='Game Detail'),
    path('account', views.detail, name="account"),
]
