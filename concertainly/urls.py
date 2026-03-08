from django.urls import path
from concertainly import views

app_name = "concertainly"

urlpatterns = [
    path('', views.home, name='home'),
    path("home/", views.home, name="home"),
    path("search/", views.search, name="search"),
    path("register/", views.register, name="register"),
    path("login/", views.login, name="login"),
    path("me/", views.account, name="account"),
    path("genres/", views.genre_list, name="genre"),
    path("genres/<str:genre_name>/", views.genre, name="genre_detail"),
    path("artist/<str:artist_name>/", views.artist, name="artist"),
    path("tour/<str:tour_name>/", views.tour, name="tour"),
]
