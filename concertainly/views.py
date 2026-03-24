from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from concertainly.models import Genre, Artist, Tour, Review, Venue
from concertainly.forms import UserForm, ReviewForm, insert_artist, insert_tour, insert_venue
from django.shortcuts import redirect 
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db.models import Count


def home(request):
    tours = (
        Tour.objects.annotate(review_count=Count("review"))
        .filter(review_count__gt=0)
        .order_by("-review_count")
    )

    highlight_tour = tours[0]
    popular_tours = tours [1:11]

    context_dict = {}
    context_dict["highlight_tour"] = highlight_tour
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
    genreObjects = Genre.objects.all()
    genres = [
        'pop', 'rnb', 'hiphop', 'rock',
        'metal', 'classical', 'jpop', 'punk',
        'kpop', 'latin', 'edm', 'mandopop'
    ]

    return render(request, "allGenres.html", {"genres": genres})

def genre(request, genre_name):
    genre = get_object_or_404(Genre, name=genre_name)

    return render(request, "genre.html", {"genre": genre})

def artist(request, artist_name):
    artist = get_object_or_404(Artist, name=artist_name)
    tours = Tour.objects.filter(artist=artist)
    context_dict = {}
    context_dict["artist"] = artist
    context_dict["tours"] = tours
    return render(request, "artist.html", context=context_dict)

def tour(request, slug):
    tour = Tour.objects.filter(slug=slug).first()
    if tour:
        reviews = Review.objects.filter(tour=tour)
    else:
        reviews = []
    return render(request, "tour.html", {"tour": tour, "reviews": reviews})

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
