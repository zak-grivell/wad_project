from django.test import TestCase
from unittest.mock import patch, Mock
from services.lastfm import LastfmApi, LAST_FM_API_KEY

class LastfmTests(TestCase):
    def setUp(self):
        self.api = LastfmApi()

    @patch(
        "services.lastfm.requests.get",
        return_value=Mock(
            json=Mock(return_value={"artist": {"name": "The Weeknd"}})
        ),
    )
    def test_artist(self, mock_get):
        MBID = "c8b03190-306c-4120-bb0b-6f2ebfc06ea9"

        artist = self.api.artist(MBID)

        self.assertEqual(artist["name"], "The Weeknd")

        mock_get.assert_called_once_with(
            "https://ws.audioscrobbler.com/2.0/",
            headers={},
            params={
                "mbid": MBID,
                "method": "artist.getInfo",
                "api_key": LAST_FM_API_KEY,
                "format": "json",
            },
        )

    @patch(
        "services.lastfm.requests.get",
        return_value=Mock(
            json=Mock(
                return_value={
                    "results": {
                        "trackmatches": {
                            "track": [{"name": "Blinding Lights"}]
                        }
                    }
                }
            )
        ),
    )
    def test_search_song(self, mock_get):
        result = self.api.search_song("Blinding Lights", "The Weeknd")

        # Because search_song returns the array at ["results"]["trackmatches"]["track"]
        self.assertEqual(result[0]["name"], "Blinding Lights")
        
        mock_get.assert_called_once_with(
            "https://ws.audioscrobbler.com/2.0/",
            headers={},
            params={
                "track": "Blinding Lights",
                "artist": "The Weeknd",
                "limit": 5,
                "method": "track.search",
                "api_key": LAST_FM_API_KEY,
                "format": "json",
            },
        )
