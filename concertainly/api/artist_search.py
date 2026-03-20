from django.http import HttpResponse
from services.spotify import SpotifyAPI
from services.ticketmaster import TicketMasterAPI
from django.http import JsonResponse

def artist_search(request):
    # sp = SpotifyAPI()

    # if not request.GET["q"] or len(request.GET["q"]) < 5:
    #     return HttpResponse(status=400)

    # artists = sp.search_artist(query=request.GET["q"])["items"]

    # return JsonResponse({ "artists": [{ "name": artist["name"], "id": artist["id"] } for artist in artists] })    
    
    sp = TicketMasterAPI()

    if not request.GET["q"] or len(request.GET["q"]) < 5:
        return HttpResponse(status=400)

    artists = sp.attraction_search({ "keyword": request.GET["q"] })

    return JsonResponse(
        {
            "artists": [
                {"name": artist["name"], "id": artist["id"]} for artist in artists
            ]
        }
    )
