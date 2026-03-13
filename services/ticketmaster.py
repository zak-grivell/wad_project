import requests
from dotenv import load_dotenv
import os
from typing import TypedDict

load_dotenv()

TICKETMATER_CONSUMER_KEY = os.getenv("TICKETMATER_CONSUMER_KEY")
URL = "https://app.ticketmaster.com/discovery/v2/"


Attraction = TypedDict(
    "Attraction",
    {
        "name": str,
        "type": str,
        "id": str,
        "test": bool,
        "locale": str,
        "images": list["Image"],
        "classifications": list["Classification"],
        "_links": "Links",
    },
)

Links = TypedDict("Links", {"self": "SelfOrAttractionOrVenue"})

Embedded = TypedDict(
    "Embedded",
    {
        "venues": list["Venue"],
        "attractions": list["Attraction"],
        "events": list["Event"],
    },
)

Location = TypedDict("Location", {"longitude": str, "latitude": str})

Address = TypedDict("Address", {"line1": str})

Country = TypedDict("Country", {"name": str, "countryCode": str})

State = TypedDict("State", {"name": str, "stateCode": str})

City = TypedDict("City", {"name": str})

Venue = TypedDict(
    "Venue",
    {
        "name": str,
        "type": str,
        "id": str,
        "test": bool,
        "locale": str,
        "postalCode": str,
        "timezone": str,
        "city": City,
        "state": State,
        "country": Country,
        "address": Address,
        "location": Location,
        "markets": list["MarketOrPromoter"],
        "_links": Links,
        "_embedded": Embedded,
    },
)

SelfOrAttractionOrVenue = TypedDict("SelfOrAttractionOrVenue", {"href": str})

Links = TypedDict(
    "Links",
    {
        "self": SelfOrAttractionOrVenue,
        "attractions": list[SelfOrAttractionOrVenue],
        "venues": list[SelfOrAttractionOrVenue],
    },
)

MarketOrPromoter = TypedDict("MarketOrPromoter", {"id": str})

NameId = TypedDict("NameId", {"id": str, "name": str})


Classification = TypedDict(
    "Classification",
    {
        "primary": bool,
        "segment": NameId,
        "genre": NameId,
        "subGenre": NameId,
    },
)

Status = TypedDict("Status", {"code": str})

Start = TypedDict(
    "Start",
    {
        "localDate": str,
        "dateTBD": bool,
        "dateTBA": bool,
        "timeTBA": bool,
        "noSpecificTime": bool,
    },
)

Dates = TypedDict("Dates", {"start": Start, "timezone": str, "status": Status})

Public = TypedDict(
    "Public", {"startDateTime": str, "startTBD": bool, "endDateTime": str}
)

Sales = TypedDict("Sales", {"public": Public})

Image = TypedDict(
    "Image", {"ratio": str, "url": str, "width": int, "height": int, "fallback": bool}
)

Event = TypedDict(
    "Event",
    {
        "name": str,
        "type": str,
        "id": str,
        "test": bool,
        "url": str,
        "locale": str,
        "images": list[Image],
        "sales": Sales,
        "dates": Dates,
        "classifications": list[Classification],
        "promoter": MarketOrPromoter,
        "_links": Links,
        "_embedded": Embedded,
    },
)

SearchFields = TypedDict(
    "SearchFields ",
    {
        "keyword": str,
        "id": str,
        "attractionId": str,
        "venueId": str,
        "postalCode": str,
        "city": str,
        "countryCode": str,
        "genreId": str,
        "size": int,
    },
)


api_params = {"apikey": TICKETMATER_CONSUMER_KEY}


class TicketMasterAPI:
    def event_search(self, params: SearchFields) -> list[Event]:
        return requests.get(f"{URL}events.json", params=params | api_params).json()[
            "_embedded"
        ]["events"]

    def event(self, id: str) -> Event:
        return requests.get(f"{URL}events/{id}.json", params=api_params).json()
    

    def attraction_search(self, params: SearchFields) -> list[Attraction]:
        return requests.get(
            f"{URL}attractions.json", params=params | api_params
        ).json()["_embedded"]["attractions"]

    def attraction(self, id: str):
        return requests.get(f"{URL}attractions/{id}.json", params=api_params).json()

    def venue_search(self, params: SearchFields) -> list[Venue]:
        return requests.get(f"{URL}venues.json", params=params | api_params).json()[
            "_embedded"
        ]["venues"]

    def venue(self, id) -> Venue:
        return requests.get(
            f"{URL}venues/{id}.json",
            params=api_params
        ).json()
