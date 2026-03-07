from django.http import HttpResponse
from django.shortcuts import render
from services.spotify import SpotifyAPI

def index(request):
    context_dict = {"boldmessage": "Crunchy, creamy, cookie, candy, cupcake!"}
    return render(request, "index.html", context=context_dict)

def spotify_test(request):
    s = SpotifyAPI()
    
    context_dict = {"boldmessage": str(s.artist("06HL4z0CvFAxyc27GXpf02"))}
    return render(request, "index.html", context=context_dict)


# Create your views here.
