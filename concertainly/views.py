from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from concertainly.models import Genre, Artist, Tour, Review
from concertainly.forms import UserForm
from django.shortcuts import redirect 
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render
from services.spotify import SpotifyAPI
from services.ticketmaster import TicketMasterAPI
from concertainly.models import *
from django.contrib.auth.decorators import login_required
from django.db.models import Count


def home(request):
    tours = (
        Tour.objects.annotate(review_count=Count("review"))
        .filter(review_count__gt=0)
        .order_by("-review_count")
    )

<<<<<<< Updated upstream
    highlight_tours = tours[:3] #top 3
    popular_tours = tours [3:13] #next top 10
=======
    highlight_tours = tours[0:3]
    popular_tours = tours [3:11]
>>>>>>> Stashed changes

    context_dict = {}
    context_dict["highlight_tours"] = highlight_tours
    context_dict["popular_tours"] = popular_tours
    context_dict["tour1"] = highlight_tours[0]
    context_dict["tour2"] = highlight_tours[1]  
    context_dict["tour3"] = highlight_tours[2]

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

    context_dict = {}
    context_dict["genre_list"] = genre_list
    context_dict["artist_list"] = artist_list

    return render(request, "search.html", context=context_dict)

def user_register(request):
    registered = False

    if request.method =='POST':
        user_form = UserForm(request.POST)

        if user_form.is_valid():
            user = user_form.save()

            user.set_password(user.password)
            user.save()

            registered = True

            return redirect("concertainly:user_login")
        else:
            print(user_form.errors)
    else:
        user_form = UserForm()
    
    return render(request,
                  "register.html",
                  context = {"user_form": user_form,
                             "registered": registered})

def spotify_test(request):
    s = SpotifyAPI()
    
    context_dict = {"boldmessage": str(s.artist("06HL4z0CvFAxyc27GXpf02"))}
    return render(request, "index.html", context=context_dict)

def user_login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                return redirect(reverse("concertainly:home"))
            else:
                return HttpResponse("Your Concertainly account is disabled.")
        else:
            print(f"Invalid login details")
            return HttpResponse("Invalid login details supplied.")
    else:
        return render(request, "login.html")

@login_required
def user_logout(request):
    logout(request)
    return redirect(reverse("concertainly:home"))

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
    tour = get_object_or_404(Tour, name=tour_name)

    return render(request, "tour_detail.html", {"tour": tour})

def ticket_master_test(request):
    return HttpResponse(str(TicketMasterAPI().attraction_search({ "keyword": "Taylor", "size": 1 })))
