from django.test import TestCase
from unittest.mock import patch, Mock
import time
from services.spotify import SpotifyAPI


class SpotifyTests(TestCase):
    def setUp(self):
        self.api = SpotifyAPI()
        self.api.access_token = "test_token"
        self.api.token_expire = time.time() + 1000

    @patch(
        "services.spotify.requests.get",
        return_value=Mock(json=Mock(return_value={"name": "Taylor Swift"})),
    )
    def test_artist_name(self, mock_get):
        ARTIST_ID = "06HL4z0CvFAxyc27GXpf02"

        artist = self.api.artist(ARTIST_ID)

        self.assertEqual(artist["name"], "Taylor Swift")

        mock_get.assert_called_once_with(
            f"https://api.spotify.com/v1/artists/{ARTIST_ID}",
            headers={'Authorization': 'Bearer test_token'},
        )

    @patch(
        "services.spotify.requests.get",
        return_value=Mock(
            json=Mock(return_value={"artists": {"items": [{"name": "Taylor Swift"}]}})
        ),
    )
    def test_search_artist(self, mock_get):
        result = self.api.search_artist("Taylor")

        self.assertEqual(result["items"][0]["name"], "Taylor Swift")

    @patch(
        "services.spotify.requests.get",
        return_value=Mock(
            json=Mock(return_value={"tracks": {"items": [{"name": "Blank Space"}]}})
        ),
    )
    def test_search_track(self, mock_get):
        result = self.api.search_track("Blank Space", artist="Taylor Swift")

        self.assertEqual(result["items"][0]["name"], "Blank Space")

    @patch(
        "services.spotify.requests.get",
        return_value=Mock(
            json=Mock(return_value={"tracks": {"items": [{"name": "Love Story"}]}})
        ),
    )
    def test_search_artist_and_song(self, mock_get):
        result = self.api.search_artist_and_song("Love Stor")

        self.assertEqual(result["items"][0]["name"], "Love Story")

    @patch(
        "services.spotify.requests.post",
        return_value=Mock(
            json=Mock(
                return_value={
                    "access_token": "new_token",
                    "expires_in": 3600,
                }
            )
        ),
    )
    def test_refresh_token(self, mock_post):
        api = SpotifyAPI()
        api.refresh_token()

        self.assertEqual(api.access_token, "new_token")
        self.assertGreater(api.token_expire, time.time())

    def test_get_access_token_does_not_refresh_if_valid(self):
        with patch.object(self.api, "refresh_token") as mock_refresh:
            token = self.api.get_access_token()

            self.assertEqual(token, {'Authorization': 'Bearer test_token'})
            mock_refresh.assert_not_called()

    def test_get_access_token_refreshes_if_expired(self):
        self.api.token_expire = 0

        with patch.object(self.api, "refresh_token") as mock_refresh:
            self.api.get_access_token()

            mock_refresh.assert_called_once()
