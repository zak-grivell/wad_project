from django import forms
from concertainly.models import Song, Review

class ReviewForm(forms.ModelForm):
    set_list = forms.ModelMultipleChoiceField(
    queryset=Song.objects.all(),
    widget = forms.CheckboxSelectMultiple,
    required = False)
    
    class Meta:
        model = Review
        fields = ['title', 
                  'thoughts', 
                  'img_path', 
                  'city', 
                  'venue', 
                  'date', 
                  'rating', 
                  'set_list']