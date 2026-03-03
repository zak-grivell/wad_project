from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    context_dict = {"boldmessage": "Crunchy, creamy, cookie, candy, cupcake!"}
    return render(request, "index.html", context=context_dict)


# Create your views here.
