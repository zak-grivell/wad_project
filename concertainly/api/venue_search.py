from django.http import HttpResponse
from services.ticketmaster import TicketMasterAPI
from django.http import JsonResponse


def venue_search(request):
    sp = TicketMasterAPI()

    if not request.GET["keyword"] or len(request.GET["keyword"]) < 3:
        return HttpResponse(status=400)

    venues = sp.venue_search({"keyword": request.GET["keyword"]})

    return JsonResponse(
        {
            "items": [
                {k: v for k, v in venue.items() if not isinstance(v, (list, dict))}
                for venue in venues
            ]
        }
    )
