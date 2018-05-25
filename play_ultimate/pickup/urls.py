from django.urls import path
# from django.contrib.auth import views as auth_views

from . import views

app_name = 'games'
urlpatterns = [
    path('', views.index, name='index'),
    path('login', views.Login.as_view(), name="login"),
    path('signup', views.Signup.as_view(), name="signup"),
    # path('logout', auth_views.logout,
    #      {'next_page', 'games:index'}, name="logout"),
    path('logout', views.Logout.as_view(), name="logout"),
    path('game/<int:game_id>', views.detail, name='Game Detail'),
    path('account', views.detail, name="account"),
    path('attendee', views.attendee, name="attendee")
]
