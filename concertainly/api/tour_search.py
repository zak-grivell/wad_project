from django.http import HttpResponse
from services.ticketmaster import TicketMasterAPI
from django.http import JsonResponse


def tour_search(request):
    sp = TicketMasterAPI()

    if not request.GET["q"] or len(request.GET["q"]) < 5:
        return HttpResponse(status=400)

    artists = sp.attraction_search({ "keyword": request.GET["q"] })

    return JsonResponse(
        {
            "artists": [
                {"name": artist["name"], "id": artist["id"]} for artist in artists
            ]
        }
    )
