from django.http import HttpResponse
from django.shortcuts import render
from concertainly.models import *
from concertainly.forms import CategoryForm
from django.shortcuts import redirect 
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from datetime import datetime


def home(request):
    return render(request, "homepage.html")

def search(request):
    return render(request, "search.html")

def register(request):
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

            if 'picture' in request.FILES:
                profile.picture = request.FILES['picture']
            
            profile.save()

            registered = True
        else:
            print(user_form.errors, profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserProfileForm()
    
    return render(request,
                  'register.html',
                  context = {'user_form': user_form,
                             'profile_form': profile_form,
                             'registered': registered})

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                return redirect(reverse('concertainly:homepage'))
            else:
                return HttpResponse("Your Concertainly account is disabled.")
        else:
            print(f"Invalid login details: {username}, {password}")
            return HttpResponse("Invalid login details supplied.")
    else:
        return render(request, 'login.html')

@login_required
def account(request):
    return render(request, "account.html")

def genre_list(request):
    return render(request, "allGenres.html")

def genre_detail(request, genre_name):
    return render(request, "genre.html", {"genre_name": genre_name})

def artist(request, artist_name):
    return render(request, "artist_detail.html", {"artist_name": artist_name})

def tour(request, tour_name):
    return render(request, "tour_detail.html", {"tour_name": tour_name})