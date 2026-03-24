from django.http import HttpResponse
from services.spotify import SPOTIFY_API
from django.http import JsonResponse


def artist_search(request):
    if not request.GET["keyword"] or len(request.GET["keyword"]) < 3:
        return HttpResponse(status=400)

    artists = SPOTIFY_API.search_track(request.GET["keyword"], artist=request.GET.get("artist", ""))

    return JsonResponse(
        {
            "items": [
                {k: v for k, v in artist.items() if not isinstance(v, (list, dict))}
                for artist in artists["items"]
            ]
        }
    )
