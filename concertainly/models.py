import uuid
from django.db.models.deletion import CASCADE
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify

class Genre(models.Model):
    id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True, primary_key = True)
    name = models.CharField(max_length=128)

class Venue(models.Model):
    id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True, primary_key = True)
    name = models.CharField(max_length=128)
    external_id = models.CharField(max_length=128)
    city = models.CharField(max_length=128)

class Artist(models.Model):
    id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True, primary_key = True)
    name = models.CharField(max_length=128)
    external_id = models.CharField(max_length=128)
    spotify_id = models.CharField(max_length=128)

    genres = models.ManyToManyField(Genre)
    slug = models.SlugField(unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

class Tour(models.Model):
    id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True, primary_key = True)
    name = models.CharField(max_length=128)
    artist = models.ForeignKey(Artist, on_delete=CASCADE)
    external_id = models.CharField(max_length=128)
    slug = models.SlugField(unique=True, blank=True)
    image = models.CharField(max_length=128, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    
class Song(models.Model):
    id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True, primary_key = True)
    name = models.CharField(max_length=128)
    artist = models.ForeignKey(Artist, on_delete=CASCADE)

    external_id = models.CharField(max_length=128)


class Review(models.Model):
    id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True, primary_key = True)
    title = models.CharField(max_length=128)
    thoughts = models.CharField(max_length=1024)
    img = models.ImageField(upload_to='reviews/', blank=True, null=True , height_field=None, width_field=None, max_length=100)

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


