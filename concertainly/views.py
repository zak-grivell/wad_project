from django.http import HttpResponse
from django.shortcuts import render
from concertainly.models import *


def index(request):
    context_dict = {"boldmessage": "Crunchy, creamy, cookie, candy, cupcake!"}
    return render(request, "index.html", context=context_dict)

def home(request):
    return render(request, "home.html")

def search(request):
    return render(request, "search.html")

def register(request):
    return render(request, "register.html")

def login(request):
    return render(request, "login.html")

def account(request):
    return render(request, "account.html")

def genre_list(request):
    return render(request, "genre_list.html")

def genre_detail(request, genre_name):
    return render(request, "genre_detail.html", {"genre_name": genre_name})

def artist_detail(request, artist_name):
    return render(request, "artist_detail.html", {"artist_name": artist_name})

def tour_detail(request, tour_name):
    return render(request, "tour_detail.html", {"tour_name": tour_name})