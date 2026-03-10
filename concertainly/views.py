from django.http import HttpResponse
from django.shortcuts import render
from services.spotify import SpotifyAPI
from concertainly.models import *
from django.contrib.auth.decorators import login_required

def home(request):
    return render(request, "homepage.html")

def search(request):
    return render(request, "search.html")

def spotify_test(request):
    s = SpotifyAPI()
    
    context_dict = {"boldmessage": str(s.artist("06HL4z0CvFAxyc27GXpf02"))}
    return render(request, "index.html", context=context_dict)

def register(request):
    return render(request, "register.html")

def login(request):
    return render(request, "login.html")

@login_required
def account(request):
    return render(request, "account.html")

def genre_list(request):
    return render(request, "allGenres.html")

def genre(request, genre_name):
    return render(request, "genre.html", {"genre_name": genre_name})

def artist(request, artist_name):
    return render(request, "artist_detail.html", {"artist_name": artist_name})

def tour(request, tour_name):
    return render(request, "tour_detail.html", {"tour_name": tour_name})

