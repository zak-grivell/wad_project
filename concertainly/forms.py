from concertainly.models import Artist, Genre, Tour, Venue
from django import forms
from django.contrib.auth.models import User
from services.lastfm import LASTFM_API
from services.spotify import SPOTIFY_API
from services.musicbrainz import MUSICBRAINZ_API
from services.ticketmaster import TICKET_MASTER_API


# deals with the information that is stored in django's User class
class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        # pretty sure email isn't necessary
        fields = (
            "username",
            "password",
        )


# we don't need an additional form because we're not storing any additional information other than what is stored on User


class DatalistWidget(forms.TextInput):
    template_name = "widgets/datalist.html"

    def __init__(self, options=None, label=None, attrs=None):
        super().__init__(attrs)
        self.options = options or []
        self.label = label or ""

    def get_context(self, name, value, attrs):
        context = super().get_context(name, value, attrs)
        context["widget"]["options"] = self.options
        context["widget"]["label"] = self.label or name.replace('_', ' ').capitalize()
        context["widget"]["datalist_id"] = attrs.get("id", name) + "_list"
        return context

class ReviewForm(forms.Form):
    title = forms.CharField(
        label="Title",
        max_length=128,
        required=True,
        widget=forms.TextInput({"class": "form-control"}),
    )
    rating = forms.ChoiceField(
        choices=[(str(n), str(n)) for n in range(1, 6)],
        widget=forms.RadioSelect(attrs={"class": "form-check-input"}),
    )
    comment = forms.CharField(
        widget=forms.Textarea(attrs={"class": "form-control", "rows": 5})
    )

    review_photo = forms.ImageField(
        allow_empty_file=True,
        required=False,
        widget=forms.FileInput(attrs={"class": "form-control"}),
    )

    date = forms.DateField(widget=forms.DateInput(attrs={"class":"form-control", "type": "date" }))

    artist_id = forms.CharField(max_length=128, widget=forms.HiddenInput())
    artist_select = forms.CharField(
        max_length=128,
        widget=DatalistWidget(
            label="Artist",
            attrs={
                "id": "artist_select",
            }
        ),
    )

    tour_id = forms.CharField(max_length=128, widget=forms.HiddenInput())
    tour_select = forms.CharField(
        max_length=128,
        widget=DatalistWidget(
            label="Tour",
            attrs={
                "id": "tour_select",
            }
        ),
    )

    venue_id = forms.CharField(max_length=128, widget=forms.HiddenInput())
    venue_select = forms.CharField(
        max_length=128,
        widget=DatalistWidget(
            label="Venue",
            attrs={
                "id": "venue_select",
            }
        ),
    )

class SearchForm(forms.Form):
    artist_id = forms.CharField(max_length=128, widget=forms.HiddenInput())
    artist_select = forms.CharField(
        max_length=128,
        widget=DatalistWidget(
            label="Artist",
            attrs={
                "id": "artist_select",
            }
        ),
        required=False
    )

    tour_id = forms.CharField(max_length=128, widget=forms.HiddenInput())
    tour_select = forms.CharField(
        max_length=128,
        widget=DatalistWidget(
            label="Tour",
            attrs={
                "id": "tour_select",
            }
        ),
        required=False
    )

    venue_id = forms.CharField(max_length=128, widget=forms.HiddenInput())
    venue_select = forms.CharField(
        max_length=128,
        widget=DatalistWidget(
            label="Venue",
            attrs={
                "id": "venue_select",
            }
        ),
        required=False
    )

def insert_artist(musicbrainz_id) -> Artist:
    artist_data = LASTFM_API.artist(musicbrainz_id)
    spotify_id = SPOTIFY_API.search_artist(artist_data["name"], 1, 0)["items"][0]["id"]
        
    db_artist = Artist.objects.create(
        external_id=musicbrainz_id,
        name=artist_data["name"],
        spotify_id=spotify_id,
    )
    db_artist.save()

    genres = Genre.objects.filter(name__in=[tag["name"] for tag in artist_data["tags"]["tag"]])

    db_artist.genres.set(genres)

    return db_artist


def insert_tour(musicbrainz_id, artist) -> Tour:
    tour = MUSICBRAINZ_API.tour(musicbrainz_id)

    db_tour = Tour.objects.create(external_id=musicbrainz_id, name=tour["name"], artist=artist)

    db_tour.save()

    return db_tour


def insert_venue(id) -> Venue:
    venue = TICKET_MASTER_API.venue(id)

    db_venue = Venue.objects.create(external_id=id, name=venue["name"])
    db_venue.save()

    return db_venue
