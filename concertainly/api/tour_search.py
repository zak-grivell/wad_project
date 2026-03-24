from concertainly.models import Tour
from django.http import HttpResponse
from django.http import JsonResponse

PARAMS = {"keyword", "venueId", "attractionId"}


def tour_search(request):
    if not request.GET["keyword"] or len(request.GET["keyword"]) < 3:
        return HttpResponse(status=400)

    tours = Tour.objects.filter(name__contains=request.GET["keyword"])

    return JsonResponse(
        {
            "items": [
                {"name": tour.name, "id": tour.id } for tour in tours
            ]
        }
    )
