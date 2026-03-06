from django.urls import path

from concertainly import views

app_name = "concertainly"
urlpatterns = [
    path("", views.homepage, name="homepage"),
]
