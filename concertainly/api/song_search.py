from django.http import HttpResponse
from services.musicbrainz import MUSICBRAINZ_API
from django.http import JsonResponse


def song_search(request):
    if not request.GET["keyword"] or len(request.GET["keyword"]) < 3:
        return HttpResponse(status=400)

    songs = MUSICBRAINZ_API.search_tracks(request.GET["keyword"], request.GET.get("artist"))

    return JsonResponse(
        {
            "items": songs
        }
    )
