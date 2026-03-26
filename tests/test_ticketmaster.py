from django.test import TestCase
from unittest.mock import patch, Mock
from services.ticketmaster import TicketMasterAPI, TICKETMATER_CONSUMER_KEY
from tests.mock_api_responces.ticketmaster import TICKET_MASTER_EVENT_SEARCH_MOCK, TICKET_MASTER_EVENT_DETAILS_MOCK, TICKET_MASTER_ATTRACTION_SEARCH_MOCK, TICKET_MASTER_ATTRACTION_DETAILS_MOCK, TICKET_MASTER_VENUE_DETAILS_MOCK, TICKET_MASTER_VENUE_SEARCH_MOCK


class SpotifyTests(TestCase):
    def setUp(self):
        self.api = TicketMasterAPI()

    @patch(
        "services.ticketmaster.requests.get",
        return_value=Mock(json=Mock(return_value=TICKET_MASTER_EVENT_SEARCH_MOCK)),
    )
    def test_event_search(self, mock_get):
        self.assertEqual(
            self.api.event_search({"keyword": "keyword", "size": 1})[0]["name"],
            "WGC Cadillac Championship - Sunday Ticket",
        )
        mock_get.assert_called_once_with(
            "https://app.ticketmaster.com/discovery/v2/events.json",
            params={
                "keyword": "keyword",
                "size": 1,
                "apikey": TICKETMATER_CONSUMER_KEY,
            },
        )

    @patch(
        "services.ticketmaster.requests.get",
        return_value=Mock(json=Mock(return_value=TICKET_MASTER_EVENT_DETAILS_MOCK)),
    )
    def test_event_details(self, mock_get):
        self.assertEqual(self.api.event("G5diZfkn0B-bh")["name"], "Radiohead")
        mock_get.assert_called_once_with(
            "https://app.ticketmaster.com/discovery/v2/events/G5diZfkn0B-bh.json",
            params = {
                'apikey':TICKETMATER_CONSUMER_KEY
            }
        )
    @patch(
        "services.ticketmaster.requests.get",
        return_value=Mock(json=Mock(return_value=TICKET_MASTER_ATTRACTION_SEARCH_MOCK)),
    )
    def test_attraction_search(self, mock_get):
        self.assertEqual(
            self.api.attraction_search({"keyword": "keyword", "size": 1})[0]["name"],
            "!!!",
        )
        mock_get.assert_called_once_with(
            "https://app.ticketmaster.com/discovery/v2/attractions.json",
            params={
                "keyword": "keyword",
                "size": 1,
                "apikey": TICKETMATER_CONSUMER_KEY,
            },
        )

    @patch(
        "services.ticketmaster.requests.get",
        return_value=Mock(json=Mock(return_value=TICKET_MASTER_ATTRACTION_DETAILS_MOCK)),
    )
    def test_attraction_details(self, mock_get):
        self.assertEqual(self.api.attraction("K8vZ9175BhV")["name"], "!!!")
        mock_get.assert_called_once_with(
            "https://app.ticketmaster.com/discovery/v2/attractions/K8vZ9175BhV.json",
            params = {
                'apikey':TICKETMATER_CONSUMER_KEY
            }
        )

    @patch(
        "services.ticketmaster.requests.get",
        return_value=Mock(json=Mock(return_value=TICKET_MASTER_VENUE_SEARCH_MOCK)),
    )
    def test_venue_search(self, mock_get):
        self.assertEqual(
            self.api.venue_search({"keyword": "keyword", "size": 1})[0]["city"]["name"],
            "Morrisburg",
        )
        mock_get.assert_called_once_with(
            "https://app.ticketmaster.com/discovery/v2/venues.json",
            params={
                "keyword": "keyword",
                "size": 1,
                "apikey": TICKETMATER_CONSUMER_KEY,
            },
        )

    @patch(
        "services.ticketmaster.requests.get",
        return_value=Mock(json=Mock(return_value=TICKET_MASTER_VENUE_DETAILS_MOCK)),
    )
    def test_venue_details(self, mock_get):
        self.assertEqual(self.api.venue("KovZpZAFnIEA")["city"]["name"], "Morrisburg")
        mock_get.assert_called_once_with(
            "https://app.ticketmaster.com/discovery/v2/venues/KovZpZAFnIEA.json",
            params = {
                'apikey':TICKETMATER_CONSUMER_KEY
            }
        )
