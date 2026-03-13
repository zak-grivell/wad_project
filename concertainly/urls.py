from django.urls import path
from concertainly import views

app_name = "concertainly"

urlpatterns = [
    path('', views.home, name='home'),
    path("home/", views.home, name="home"),
    path("search/", views.search, name="search"),
    path("register/", views.user_register, name="register"),
    path("login/", views.user_login, name="login"),
    path("me/", views.account, name="account"),
    path("genres/", views.genre_list, name="genres"),
    path("genres/<str:genre_name>/", views.genre, name="genre"),
    path("artist/<str:artist_name>/", views.artist, name="artist"),
    path("tour/<str:tour_name>/", views.tour, name="tour"),
    path("ticket", views.ticket_master_test)
    path("logout/", views.user_logout, name="logout"),
]
