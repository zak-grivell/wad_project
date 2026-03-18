import uuid
from django.db.models.deletion import CASCADE
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
<<<<<<< HEAD
from django.template.defaultfilters import slugify
=======
from django.contrib.auth.models import User

>>>>>>> 4bb8586baa4e541f373dd61b568e374618dd0c20

class Artist(models.Model):
    id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True, primary_key = True)
    name = models.CharField(max_length=128)
    spotify_id = models.CharField(max_length=128)

class Tour(models.Model):
    id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True, primary_key = True)
    name = models.CharField(max_length=128)
    artist = models.ForeignKey(Artist, on_delete=CASCADE)
<<<<<<< HEAD
    slug = models.SlugField(unique = True)
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Tour, self).save(*args, **kwargs)

    def __str__(self):
        return self.name

=======
    ticket_master_id = models.CharField(max_length=128)
>>>>>>> 4bb8586baa4e541f373dd61b568e374618dd0c20

class Song(models.Model):
    id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True, primary_key = True)
    name = models.CharField(max_length=128)
    artist = models.ForeignKey(Artist, on_delete=CASCADE)

    spotify_id = models.CharField(max_length=128)


class Review(models.Model):
    id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True, primary_key = True)
    title = models.CharField(max_length=128)
    thoughts = models.CharField(max_length=1024)
    img = models.ImageField(upload_to='reviews/', blank=True, null=True , height_field=None, width_field=None, max_length=100)

    city = models.CharField(max_length=128)
    venue = models.CharField(max_length=128)
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


class Genre(models.Model):
    id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True, primary_key = True)
    name = models.CharField(max_length=128)
