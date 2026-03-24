from django.contrib import admin
from concertainly.models import Review, Artist, Genre, Venue, Tour, Song

admin.site.register(Review)
admin.site.register(Artist)
admin.site.register(Genre)
admin.site.register(Venue)
admin.site.register(Tour)
admin.site.register(Song)
