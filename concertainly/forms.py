from django import forms
from django.contrib.auth.models import User

# deals with the information that is stored in django's User class
class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        # pretty sure email isn't necessary
        fields = ('username', 'password',)

# we don't need an additional form because we're not storing any additional information other than what is stored on User
