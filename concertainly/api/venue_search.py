from django.http import HttpResponse
from services.ticketmaster import TicketMasterAPI
from django.http import JsonResponse
from services.musicbrainz import search_venues


def venue_search(request):
    if not request.GET["keyword"] or len(request.GET["keyword"]) < 3:
        return HttpResponse(status=400)

    venues = TicketMasterAPI().venue_search(params = {"keyword":request.GET["keyword"] })

    return JsonResponse(
        {
            "items": venues
        }
    )
