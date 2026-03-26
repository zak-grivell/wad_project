from django.test import TestCase
from unittest.mock import patch, Mock
from services.musicbrainz import MusicbrainzApi 

class MusicbrainzTests(TestCase):
    def setUp(self):
        self.api = MusicbrainzApi()

    @patch(
        "services.musicbrainz.requests.get",
        return_value=Mock(json=Mock(return_value={"name": "Taylor Swift", "id": "123"})),
    )
    def test_artist(self, mock_get):
        MBID = "123"

        artist = self.api.artist(MBID)

        self.assertEqual(artist["name"], "Taylor Swift")

        mock_get.assert_called_once_with(
            f"https://musicbrainz.org/ws/2/artist/{MBID}",
            headers={"User-Agent": "Concertainly/0 ( 3013507g@student.gla.ac.uk )"},
            params={"inc": "tags+url-rels", "fmt": "json"},
        )

    @patch(
        "services.musicbrainz.requests.get",
        return_value=Mock(json=Mock(return_value={"name": "Eras Tour"})),
    )
    def test_tour(self, mock_get):
        MBID = "456"
        tour = self.api.tour(MBID)

        self.assertEqual(tour["name"], "Eras Tour")

    @patch(
        "services.musicbrainz.requests.get",
        return_value=Mock(json=Mock(return_value={"name": "Wembley Stadium"})),
    )
    def test_venue(self, mock_get):
        MBID = "789"
        venue = self.api.venue(MBID)

        self.assertEqual(venue["name"], "Wembley Stadium")

    @patch(
        "services.musicbrainz.requests.get",
        return_value=Mock(
            json=Mock(return_value={"artists": [{"name": "Taylor Swift"}]})
        ),
    )
    def test_search_artists(self, mock_get):
        result = self.api.search_artists("Taylor")

        self.assertEqual(result[0]["name"], "Taylor Swift")

    @patch(
        "services.musicbrainz.requests.get",
        return_value=Mock(
            json=Mock(return_value={"series": [{"name": "Eras Tour"}]})
        ),
    )
    def test_search_tours(self, mock_get):
        result = self.api.search_tours("Eras Tour", artist_id="123")

        self.assertEqual(result[0]["name"], "Eras Tour")

    @patch(
        "services.musicbrainz.requests.get",
        return_value=Mock(
            json=Mock(return_value={"places": [{"name": "Wembley Stadium"}]})
        ),
    )
    def test_search_venues(self, mock_get):
        result = self.api.search_venues("Wembley")

        self.assertEqual(result[0]["name"], "Wembley Stadium")

    @patch(
        "services.musicbrainz.requests.get",
        return_value=Mock(
            json=Mock(return_value={"recordings": [{"title": "Blank Space"}]})
        ),
    )
    def test_search_tracks(self, mock_get):
        result = self.api.search_tracks("Blank Space", artist_id="123")

        self.assertEqual(result[0]["title"], "Blank Space")
