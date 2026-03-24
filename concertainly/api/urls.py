from django.urls import path
from concertainly.api.artist_search import artist_search
from concertainly.api.tour_search import tour_search
from concertainly.api.venue_search import venue_search

urlpatterns = [
    path('artist_search', artist_search, name='artist_search_api'),
    path('tour_search', tour_search, name='tour_search_api'),
    path('venue_search', venue_search, name='venue_search_api'),
]
