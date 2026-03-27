from django.urls import path, include
from concertainly import views

app_name = "concertainly"

urlpatterns = [
    path('', views.home, name='home'),
    path("home/", views.home, name="home"),
    path("search/", views.search, name="search"),
    path("search_results/", views.search_results, name="search_results"),
    path("register/", views.user_register, name="register"),
    path("login/", views.user_login, name="login"),
    path("genres/", views.genre_list, name="genres"),
    path("genres/<str:genre_name>/", views.genre, name="genre"),
    path("artist/<slug:slug>/", views.artist, name="artist"),
    path("artist/", views.redirect_page),
    path("tour/<slug:slug>/", views.tour, name="tour"),
    path("tour/", views.redirect_page),
    path("logout/", views.user_logout, name="logout"),    
    path("review/", views.review, name="review"),
    path("review/<slug:slug>/", views.review, name="review_with_slug"),
    path("api/", include("concertainly.api.urls"), name="api"),
]
