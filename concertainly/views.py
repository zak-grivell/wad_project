from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from concertainly.models import Genre, Artist, Tour
from django.shortcuts import redirect 
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


def home(request):
    tours = Tour.objects.order_by("-reviews") #needs reviews attribute in tours

    highlight_tours = tours[:3] #top 3
    popular_tours = tours [3:13] #next top 10

    context_dict = {}
    context_dict["highlight"] = highlight_tours
    context_dict["popular"] = popular_tours

    return render(request, "homepage.html", context=context_dict)

def search(request):
    return render(request, "search.html")

def user_register(request):
    return render(request, "register.html")

def user_login(request):
    return render(request, "login.html")

@login_required
def user_logout(request):
    logout(request)
    return redirect(reverse("concertainly:home"))

@login_required
def account(request):
    return render(request, "account.html")

def genre_list(request):
    return render(request, "allGenres.html")

def genre(request, genre_name):
    genre = get_object_or_404(Genre, name=genre_name)

    return render(request, "genre.html", {"genre": genre})

def artist(request, artist_name):
    artist = get_object_or_404(Artist, name=artist_name)

    return render(request, "artist.html", {"artist": artist})

def tour(request, tour_name):
    tour = get_object_or_404(Tour, name=tour_name)

    return render(request, "tour_detail.html", {"tour": tour})