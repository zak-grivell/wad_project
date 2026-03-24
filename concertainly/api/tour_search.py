from concertainly.models import Tour
from django.http import HttpResponse
from services.musicbrainz import search_tours
from django.http import JsonResponse

PARAMS = {"keyword", "venueId", "attractionId"}


def tour_search(request):
    if not request.GET["keyword"] or len(request.GET["keyword"]) < 3:
        return HttpResponse(status=400)

    tours = search_tours(request.GET["keyword"], request.GET.get("artistId"))

    print(tours)

    return JsonResponse(
        {
            "items": tours        }
    )

