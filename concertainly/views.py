from django.http import HttpResponse


def index(request):
    return HttpResponse("Concertainly says hey there partner!")


# Create your views here.
