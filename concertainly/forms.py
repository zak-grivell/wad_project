from django import forms
from django.contrib.auth.models import User
from concertainly.models import Artist, Tour, Venue, Genre

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
        self.label = label or ""

    def get_context(self, name, value, attrs):
        context = super().get_context(name, value, attrs)
        context["widget"]["label"] = self.label or name.replace('_', ' ').capitalize()
        context["widget"]["datalist_id"] = attrs.get("id", name) + "_list"
        return context

class SetListWidget(forms.SelectMultiple):
    template_name = "widgets/setlist.html"

    def __init__(self, choices=[], attrs={}):
        super().__init__()
        self.choices = list(choices)

    def get_context(self, name, value, attrs):
        context = super().get_context(name, value, attrs)

        if value is None:
            value = []
        value = set(str(v) for v in value)

        context["widget"]["choices"] = [
            {
                "value": f"{option_value}|{option_label}",
                "label": option_label,
                "selected": str(option_value) in value,
            }
            for option_value, option_label in self.choices
        ]
        context["widget"]["disabled"] = attrs.get("disabled", False)

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
        disabled=True,
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

    setlist = forms.MultipleChoiceField(widget=SetListWidget(), choices=[], disabled=True, required=False)


class SearchForm(forms.Form):
    artist_id = forms.CharField(max_length=128, widget=forms.HiddenInput(), required=False)
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

    tour_id = forms.CharField(max_length=128, widget=forms.HiddenInput(), required=False)
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

    venue_id = forms.CharField(max_length=128, widget=forms.HiddenInput(), required=False)
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

    genre_id = forms.CharField(max_length=128, widget=forms.HiddenInput(), required=False)
    genre_select = forms.CharField(
        max_length=128,
        widget=DatalistWidget(
            label="Genre",
            attrs={
                "id": "genre_select",
            }
        ),
        required=False
    )

    date = forms.DateField(widget=forms.DateInput(attrs={"class":"form-control", "type": "date" }), required=False)
