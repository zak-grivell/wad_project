import uuid
from django.db.models.deletion import CASCADE
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.contrib.auth.models import User

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
    image_src = models.CharField(max_length=128)

    genres = models.ManyToManyField(Genre)

class Tour(models.Model):
    id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True, primary_key = True)
    name = models.CharField(max_length=128)
    artist = models.ForeignKey(Artist, on_delete=CASCADE)
    external_id = models.CharField(max_length=128)

    
class Song(models.Model):
    id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True, primary_key = True)
    name = models.CharField(max_length=128)
    artist = models.ForeignKey(Artist, on_delete=CASCADE)

    external_id = models.CharField(max_length=128)


class Review(models.Model):
    id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True, primary_key = True)
    title = models.CharField(max_length=128)
    thoughts = models.CharField(max_length=1024)
    img = models.ImageField(blank=True)

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


