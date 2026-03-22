from django.http import HttpResponse
from services.spotify import SpotifyAPI
from django.http import JsonResponse


def artist_search(request):
    sp = SpotifyAPI()

    if not request.GET["keyword"] or len(request.GET["keyword"]) < 3:
        return HttpResponse(status=400)

    artists = sp.search_artist(request.GET["keyword"])

    return JsonResponse(
        {
            "items": [
                {k: v for k, v in artist.items() if not isinstance(v, (list, dict))}
                for artist in artists["items"]
            ]
        }
    )
