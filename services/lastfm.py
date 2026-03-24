import requests
from dotenv import load_dotenv
import os
import logging

logging.basicConfig(level=logging.DEBUG)

logging.getLogger("urllib3").setLevel(logging.DEBUG)


load_dotenv()

LAST_FM_API_KEY= os.getenv("LAST_FM_API_KEY")
BASE_URL = "https://ws.audioscrobbler.com/2.0/"

class LastfmApi:
    def request(self, path, headers={}, params={}):
        return requests.get(
            f"{BASE_URL}",
            headers=headers,
            params=params | { "method": path } | {"api_key": LAST_FM_API_KEY, "format": "json"},
        ).json()

    def artist(self, id: str):
        return self.request("artist.getInfo", params={"mbid": id})["artist"]

LASTFM_API = LastfmApi()
