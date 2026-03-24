from django.http import HttpResponse
from services.ticketmaster import TICKET_MASTER_API
from django.http import JsonResponse


def venue_search(request):
    if not request.GET["keyword"] or len(request.GET["keyword"]) < 3:
        return HttpResponse(status=400)

    venues = TICKET_MASTER_API.venue_search(params = {"keyword":request.GET["keyword"] })
    
    return JsonResponse(
        {
            "items": venues
        }
    )
