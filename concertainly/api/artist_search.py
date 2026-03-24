from django.http import HttpResponse
from services.musicbrainz import MUSICBRAINZ_API
from django.http import JsonResponse


def artist_search(request):
    if not request.GET["keyword"] or len(request.GET["keyword"]) < 3:
        return HttpResponse(status=400)

    artists = MUSICBRAINZ_API.search_artists(request.GET["keyword"])

    return JsonResponse(
        {
            "items": artists
        }
    )
