import requests

BASE_URL = "https://musicbrainz.org/ws/2"


def request(path, headers={}, params={}):
    print(params | {"fmt": "json"})
    return requests.get(
        f"{BASE_URL}/{path}",
        headers={"User-Agent": "Concertainly/0 ( 3013507g@student.gla.ac.uk )"}
        | headers,
        params=params | {"fmt": "json"},
    ).json()

def get_artist_by_id(mbid):
    return request(f"artist/{mbid}", params={"inc": "tags+url-rels",})

def get_tour_by_id(mbid):
    return request(f"series/{mbid}")

def get_venue_by_id(mbid):
    return request(f"place/{mbid}")

def search_artists(query):
    return request("artist", params={
        "query": query,
        "limit": 5,
    }).get("artists", [])

def search_tours(tour_name, artist_id=None):
    query = f'series:"{tour_name}" AND type:Tour'
    if artist_id:
            query += f' AND arid:{artist_id}'

    return request("series", params={"query": query}).get("series", [])

def search_venues(search_term):
    query = f'place:"{search_term}" OR alias:"{search_term}" OR comment:"{search_term}"'        
    return request("place", params={"query": query}).get("places", [])

if __name__ == "__main__":
    t = get_artist_by_id("20244d07-534f-4eff-b4d4-930878889970")

    print(t)
