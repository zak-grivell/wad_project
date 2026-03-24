from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from concertainly.models import Genre, Artist, Tour, Review, Venue
from concertainly.forms import UserForm, ReviewForm, insert_artist, insert_tour, insert_venue
from django.shortcuts import redirect 
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout, get_user_model
from services.spotify import SpotifyAPI
from services.ticketmaster import TicketMasterAPI
from django.contrib.auth.decorators import login_required
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

    context_dict = {}
    context_dict["genre_list"] = genre_list
    context_dict["artist_list"] = artist_list

    return render(request, "search.html", context=context_dict)

def user_register(request):
    registered = False
    print("in register")
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
            print("registered successfully")
        else:
            # if invalid, complain to the terminal
            print(user_form.errors)
    else:
        user_form = UserForm()

    return render(request, 'register.html', context = {'user_form': user_form, 'registered': registered})

def spotify_test(request):
    s = SpotifyAPI()
    
    context_dict = {"boldmessage": str(s.artist("06HL4z0CvFAxyc27GXpf02"))}
    return HttpResponse(str(context_dict))

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

@login_required
def review(request):
    if (request.method == "POST"):
        form = ReviewForm(request.POST, request.FILES)

        if form.is_valid():
            artist_query = Artist.objects.filter(external_id=form.cleaned_data["artist_id"])
            artist = artist_query.first() if artist_query.exists() else insert_artist(form.cleaned_data['artist_id'])

            tour_query = Tour.objects.filter(external_id=form.cleaned_data["tour_id"])
            tour = tour_query.first() if tour_query.exists() else insert_tour(form.cleaned_data['tour_id'], artist=artist)
            
            venue_query = Venue.objects.filter(external_id=form.cleaned_data["venue_id"])
            venue = venue_query.first() if venue_query.exists() else insert_venue(form.cleaned_data['venue_id'])
            
            Review.objects.create(
                title=form.cleaned_data["title"],
                thoughts=form.cleaned_data["comment"],
                date=form.cleaned_data["date"],
                rating=form.cleaned_data["rating"],
                img=form.cleaned_data["review_photo"],
                tour=tour,
                venue=venue,
                user=request.user
             )

            return redirect(f"{reverse("tour")}/{tour.name}")  # ty:ignore[unresolved-attribute]
        else:
            print(form.errors)
    else:
        form = ReviewForm()
    
    return render(request, "review.html", {"form": form})
