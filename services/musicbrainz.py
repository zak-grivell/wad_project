import requests

BASE_URL = "https://musicbrainz.org/ws/2"

class MusicbrainzApi:
    def request(self, path, headers={}, params={}):
        print(params | {"fmt": "json"})
        return requests.get(
            f"{BASE_URL}/{path}",
            headers={"User-Agent": "Concertainly/0 ( 3013507g@student.gla.ac.uk )"}
            | headers,
            params=params | {"fmt": "json"},
        ).json()

    def artist(self, mbid):
        return self.request(
            f"artist/{mbid}",
            params={
                "inc": "tags+url-rels",
            },
        )

    def tour(self, mbid):
        return self.request(f"series/{mbid}")

    def venue(self, mbid):
        return self.request(f"place/{mbid}")

    def search_artists(self, query):
        return self.request(
            "artist",
            params={
                "query": query,
                "limit": 5,
            },
        ).get("artists", [])

    def search_tours(self, tour_name, artist_id=None):
        query = f'series:"{tour_name}" AND type:Tour'
        if artist_id:
            query += f" AND arid:{artist_id}"

        return self.request("series", params={"query": query}).get("series", [])

    def search_venues(self, search_term):
        query = (
            f'place:"{search_term}" OR alias:"{search_term}" OR comment:"{search_term}"'
        )
        return self.request("place", params={"query": query}).get("places", [])


    def search_tracks(self, track_name, artist_id=None):
        fuzzy_terms = " ".join(f"{word}~" for word in track_name.split())
        
        query = f'recording:({fuzzy_terms})'
        if artist_id:
            query += f" AND arid:{artist_id}"

        res=  self.request(
            "recording",
            params={
                "query": query,
                "limit": 10,
            },
        )

        print(res)
            
        return res["recordings"]

MUSICBRAINZ_API = MusicbrainzApi()
