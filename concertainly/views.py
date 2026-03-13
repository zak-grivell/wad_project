from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from concertainly.models import Genre, Artist, Tour, Review
from concertainly.forms import UserForm
from django.shortcuts import redirect 
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render
from services.spotify import SpotifyAPI
from concertainly.models import *
from django.contrib.auth.decorators import login_required
from concertainly.forms import UserForm
from django.db.models import Count


def home(request):
    tours = (
        Tour.objects.annotate(review_count=Count("review"))
        .filter(review_count__gt=0)
        .order_by("-review_count")
    )

    highlight_tours = tours[:3] #top 3
    popular_tours = tours [3:13] #next top 10

    context_dict = {}
    context_dict["highlight_tours"] = highlight_tours
    context_dict["popular_tours"] = popular_tours

    return render(request, "homepage.html", context=context_dict)

def search(request):
    genre_list = (
        Genre.objects.annotate(review_count=Count("review"))
        .filter(review_count__gt=0)
        .order_by("-review_count")[:10]
    )
    artist_list = (
        Tour.objects.annotate(review_count=Count("review"))
        .filter(review_count__gt=0)
        .order_by("-review_count")[:10]
    )

def login(request):
    return render(request, "login.html")

@login_required
def account(request):
    return render(request, "account.html")

def genre_list(request):
    genres = Genre.objects.all()

    return render(request, "allGenres.html", {"genres": genres})

def genre(request, genre_name):
    genre = get_object_or_404(Genre, name=genre_name)

    return render(request, "genre.html", {"genre": genre})

def artist(request, artist_name):
    artist = get_object_or_404(Artist, name=artist_name)

    return render(request, "artist.html", {"artist": artist})

def tour(request, tour_name):
    return render(request, "tour_detail.html", {"tour_name": tour_name})

def register(request):
    registered = False
    
    # if it's a post request, process the data
    if request.method == "POST":
        # grab form data
        user_form = UserForm(request.POST)

        # NOTE: if we ever add more info on each user (necessitating the existence of ConcertUser or something) we'll need a new form and a check that it's valid
        if user_form.is_valid():
            # save data
            user = user_form.save()

            # set_password does password hashing
            user.set_password(user.password)
            user.save()

            registered = True
        else:
            # if invalid, complain to the terminal
            print(user_form.errors)
    else:
        user_form = UserForm()

    return render(request, 'conertainly/register.html', context = {'user_form': user_form, 'registered': registered})
