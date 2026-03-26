import time
import requests
from dotenv import load_dotenv
import os
from typing import TypedDict, Literal

Image = TypedDict("Image", {"height": int, "url": str, "width": int})

Followers = TypedDict("Followers", {"href": None, "total": int})

Image = TypedDict("Image", {"height": int, "width": int, "url": str})

TrackArtist = TypedDict("TrackArtist", {"id": str, "name": str, "type": str})

Album = TypedDict(
    "Album",
    {
        "album_type": str,
        "artists": list[TrackArtist],
        "href": str,
        "id": str,
        "images": list[Image],
        "is_playable": bool,
        "name": str,
        "release_date": str,
        "release_date_precision": str,
        "total_tracks": int,
        "type": str,
    },
)

SpotifyTrack = TypedDict(
    "SpotifyTrack ",
    {
        "album": Album,
        "artists": list['SpotifyArtist'],
        "disc_number": int,
        "duration_ms": int,
        "explicit": bool,
        "id": str,
        "name": str,
        "popularity": int,
        "track_number": int,
        "type": str,
    },
)

SearchType = Literal["track", "artist"]


SpotifyArtist = TypedDict(
    "SpotifyArtist",
    {
        "genres": list[str],
        "id": str,
        "images": list[Image],
        "name": str,
        "popularity": str,
    },
)

ArtistSearchResult = TypedDict(
    "ArtistSearchResult ",
    {"limit": int, "offset": int, "total": int, "items": list[SpotifyArtist]},
)
TrackSearchResult = TypedDict(
    "TrackSearchResult",
    {"limit": int, "offset": int, "total": int, "items": list[SpotifyTrack]},
)

SpotifySearch = TypedDict(
    "SpotifySearch ", {"tracks": TrackSearchResult, "artists": ArtistSearchResult}
)

load_dotenv()

SPOTIFY_CLIENT_ID = os.getenv("SPOTIFY_CLIENT_ID")
SPOTIFY_CLIENT_SECRET = os.getenv("SPOTIFY_CLIENT_SECRET")


class SpotifyAPI:
    token_expire = 0
    access_token = ""
    
    def refresh_token(self):
        result = requests.post(
            "https://accounts.spotify.com/api/token",
            headers={
                "Content-Type": "application/x-www-form-urlencoded",
            },
            data={
                "client_id": SPOTIFY_CLIENT_ID,
                "client_secret": SPOTIFY_CLIENT_SECRET,
                "grant_type": "client_credentials",
            },
        ).json()

        self.access_token = result["access_token"]
        self.token_expire = time.time() + result["expires_in"]

    def get_access_token(self) -> dict:
        if not self.access_token or time.time() >= self.token_expire:
            self.refresh_token()

        return { "Authorization": f"Bearer {self.access_token}" }
        

    def artist(self, artist_id: str) -> SpotifyArtist:
        return requests.get(
            f"https://api.spotify.com/v1/artists/{artist_id}",
            headers=self.get_access_token(),
        ).json()

    def search_artist(
        self, query: str, limit: int = 5, offset: int = 0
    ) -> ArtistSearchResult:
        data = requests.get(
            "https://api.spotify.com/v1/search",
            headers=self.get_access_token(),
            params={
                "q": query,
                "type": ["artist"],
                "market": "gb",
                "limit": limit,
                "offset": offset,
            },
        ).json()

        print(data)
        
        return data["artists"]

    def search_track(
        self, query: str, artist: str, limit: int = 5, offset: int = 0
    ) -> TrackSearchResult:
        return requests.get(
            "https://api.spotify.com/v1/search",
            headers=self.get_access_token(),
            params={
                "q": query + (f" artist:{artist}" if artist else ""),
                "type": "track",
                "market": "gb",
                "limit": limit,
                "offset": offset,
            },
        ).json()["tracks"]

    def search_artist_and_song(
        self, query: str, limit: int = 5, offset: int = 0
    ) -> SpotifySearch:
        return requests.get(
            "https://api.spotify.com/v1/search",
            headers=self.get_access_token(),
            params={
                "q": query,
                "type": ["track", "artist"],
                "market": "gb",
                "limit": limit,
                "offset": offset,
            },
        ).json()["tracks"]

    def artist_image(self, artist_id) -> str:
        return self.artist(artist_id)["images"][-1]["url"]

SPOTIFY_API = SpotifyAPI()

if __name__ == "__main__":
    A = []

    A.append("6qqNVTkY8uBg9cP3Jd7DAH") 
    A.append("6XyY86QOPPrYVGvF9ch6wz") 
    A.append("06HL4z0CvFAxyc27GXpf02") 
    A.append("6KImCVD70vtIoJWnq6nGn3") 
    A.append("1McMsnEElThX1knmY4oliG") 
    A.append("74KM79TiuVKeVCqs8QtB0B") 
    A.append("4Uc8Dsxct0oMqx0P6i60ea") 
    A.append("1Hsdzj7Dlq2I7tHP7501T4") 
    A.append("4G9NDjRyZFDlJKMRL8hx3S")
    A.append("7aRC4L63dBn3CiLDuWaLSI")

    for a in A:
        a = SPOTIFY_API.artist(a)

        print(a["images"][0]["url"])
