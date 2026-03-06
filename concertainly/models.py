import uuid
from django.db.models.deletion import CASCADE
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.contrib.auth.models import User


class Artist(models.Model):
    id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True, primary_key = True)
    name = models.CharField(max_length=128)


class ConcertUser(models.Model):
    # associate a ConcertUser to each user
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True, primary_key = True)
    
    def __str__(self):
        return self.user.username

class Tour(models.Model):
    id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True, primary_key = True)
    name = models.CharField(max_length=128)
    artist = models.ForeignKey(Artist, on_delete=CASCADE)


class Song(models.Model):
    id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True, primary_key  = True)
    name = models.CharField(max_length=128)
    artist = models.ForeignKey(Artist, on_delete=CASCADE)


class Review(models.Model):
    id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True, primary_key  = True)
    title = models.CharField(max_length=128)
    thoughts = models.CharField(max_length=1024)
    img_path = models.CharField(max_length=128)

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


class Genre:
    id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True, primary_key  = True)
    name = models.CharField(max_length=128)
