import uuid
from django.db.models.deletion import CASCADE
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
from services.lastfm import LASTFM_API
from services.spotify import SPOTIFY_API
from services.ticketmaster import TICKET_MASTER_API
from services.musicbrainz import MUSICBRAINZ_API


class Genre(models.Model):
    id = models.UUIDField(
        default=uuid.uuid4, editable=False, unique=True, primary_key=True
    )
    name = models.CharField(max_length=128)
    nice_name = models.CharField(max_length=128, default="")

    def genre_name(self):
        return str(self.name)
    
    def genre_nice_name(self):
        return str(self.nice_name)


class VenueManager(models.Manager):
    def get_or_create_from_api(self, ticketmaster_id):
        venue, created = self.get_or_create(external_id=ticketmaster_id)

        if created:
            venue_data = TICKET_MASTER_API.venue(ticketmaster_id)

            venue.name = venue_data.get("name", "Unknown Venue")
            venue.save()

        return venue


class Venue(models.Model):
    objects = VenueManager()

    id = models.UUIDField(
        default=uuid.uuid4, editable=False, unique=True, primary_key=True
    )
    name = models.CharField(max_length=128)
    external_id = models.CharField(max_length=128)
    city = models.CharField(max_length=128)

    def __str__(self):
        return f"{self.name}, {self.city}"

class ArtistManager(models.Manager):
    def get_or_create_from_api(self, musicbrainz_id: str) -> "Artist":
        artist = self.filter(external_id=musicbrainz_id).first()
        if artist:
            return artist

        artist_data = LASTFM_API.artist(musicbrainz_id)
        spotify_results = SPOTIFY_API.search_artist(artist_data["name"], 1, 0)

        artist, created = self.get_or_create(
            external_id=musicbrainz_id,
            defaults={
                "name": artist_data["name"],
                "spotify_image": spotify_results["items"][0]["images"][0]["url"],
            },
        )

        tag_names = [tag["name"] for tag in artist_data["tags"]["tag"]]
        genres = Genre.objects.filter(name__in=tag_names)
        artist.genres.set(genres)
        artist.save()

        return artist


class Artist(models.Model):
    objects = ArtistManager()

    id = models.UUIDField(
        default=uuid.uuid4, editable=False, unique=True, primary_key=True
    )
    name = models.CharField(max_length=128)
    external_id = models.CharField(max_length=128)

    spotify_image = models.CharField(max_length=128)
    genres = models.ManyToManyField(Genre)
    slug = models.SlugField(unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)
    def __str__(self):
        return self.name

class TourManager(models.Manager):
    def get_or_create_from_api(
        self, musicbrainz_id: str, artist_instance: Artist
    ) -> "Tour":
        tour = self.filter(external_id=musicbrainz_id).first()
        if tour:
            return tour

        tour_data = MUSICBRAINZ_API.tour(musicbrainz_id)

        tour, created = self.get_or_create(
            external_id=musicbrainz_id,
            defaults={"artist": artist_instance, "name": tour_data["name"]},
        )

        return tour



class Tour(models.Model):
    objects = TourManager()

    id = models.UUIDField(
        default=uuid.uuid4, editable=False, unique=True, primary_key=True
    )
    name = models.CharField(max_length=128)
    artist = models.ForeignKey(Artist, on_delete=CASCADE)
    external_id = models.CharField(max_length=128)
    slug = models.SlugField(unique=True, blank=True)
    image = models.CharField(max_length=128, blank=True)

    def save(self, *args, **kwargs):
        print(self.name)

        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)


    def __str__(self):
        return self.name

    
class Song(models.Model):
    id = models.UUIDField(
        default=uuid.uuid4, editable=False, unique=True, primary_key=True
    )
    name = models.CharField(max_length=128)
    artist = models.ForeignKey(Artist, on_delete=CASCADE)

    external_id = models.CharField(max_length=128)


class Review(models.Model):
    id = models.UUIDField(
        default=uuid.uuid4, editable=False, unique=True, primary_key=True
    )
    title = models.CharField(max_length=128)
    thoughts = models.CharField(max_length=1024)
    img = models.ImageField(
        upload_to="reviews/",
        blank=True,
        null=True,
        height_field=None,
        width_field=None,
        max_length=100,
    )

    venue = models.ForeignKey(Venue, on_delete=CASCADE)
    date = models.DateField()

    rating = models.IntegerField(
        validators=[
            MinValueValidator(0),
            MaxValueValidator(5),
        ]
    )

    user = models.ForeignKey(User, on_delete=CASCADE)
    tour = models.ForeignKey(Tour, on_delete=CASCADE)

    set_list = models.ManyToManyField(Song)

    def artist(self):
        return self.tour.artist
    
    def __str__(self):
        return "Review: ID - " + str(self.id) + ", Title - " + str(self.title) + ", Venue - " + str(self.venue) + ", Date - " + str(self.date) + ", Artist - " + str(self.artist()) + ", Tour - " + str(self.tour)

    def genres(self):
        return [genre for genre in self.artist().genres.all()]
    
    def genre_name_list(self):
        return [g.genre_name() for g in self.genres()]
    
    def genre_nice_name_list(self):
        return [g.genre_nice_name() for g in self.genres()]
    
    def genres_allnames_string(self):
        return ", ".join([g.genre_name() for g in self.genres()])