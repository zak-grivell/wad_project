from django.http import HttpResponse
from services.musicbrainz import MUSICBRAINZ_API
from django.http import JsonResponse

PARAMS = {"keyword", "venueId", "attractionId"}


def tour_search(request):
    if not request.GET["keyword"] or len(request.GET["keyword"]) < 3:
        return HttpResponse(status=400)

    tours = MUSICBRAINZ_API.search_tours(
        request.GET["keyword"], request.GET.get("artistId")
    )

    return JsonResponse({"items": tours})
