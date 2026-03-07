from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from concertainly.models import Genre, Artist, Tour
from concertainly.forms import UserForm, UserProfileForm
from django.shortcuts import redirect 
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


def home(request):
    tours = Tour.objects.order_by("-reviews") #needs reviews attribute in tours

    highlight_tours = tours[:3] #top 3
    popular_tours = tours [3:13] #next top 10

    context_dict = {}
    context_dict["highlight_tours"] = highlight_tours
    context_dict["popular_tours"] = popular_tours

    return render(request, "homepage.html", context=context_dict)

def search(request):
    #needs entries (total number of reviews) attribute
    genre_list = Genre.objects.order_by("-entries")[:10] 
    artist_list = Artist.objects.order_by("-entries")[:10]

    context_dict = {}
    context_dict["genre_list"] = genre_list
    context_dict["artist_list"] = artist_list

    return render(request, "search.html", context=context_dict)

def user_register(request):
    registered = False

    if request.method =='POST':
        user_form = UserForm(request.POST)
        profile_form = UserProfileForm(request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()

            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user
            
            profile.save()

            registered = True

            return redirect("concertainly:user_login")
        else:
            print(user_form.errors, profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserProfileForm()
    
    return render(request,
                  "register.html",
                  context = {"user_form": user_form,
                             "profile_form": profile_form,
                             "registered": registered})

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