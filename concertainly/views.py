from django.http import HttpResponse
from django.shortcuts import render
from concertainly.forms import UserForm

def homepage(request):
    return render(request, "homepage.html")

def register(request):
    registered = False
    
    # if it's a post request, process the data
    if request.method == "POST":
        # grab form data
        user_form = UserForm(request.POST)

        # NOTE: if we ever add more info on each user (necessitating the existence of ConcertUser or something) we'll need a new form and a check that it's valid
        if user_form.is_valid():
            # save data
            user = user_form.save()

            # set_password does password hashing
            user.set_password(user.password)
            user.save()

            registered = True
        else:
            # if invalid, complain to the terminal
            print(user_form.errors)
    else:
        user_form = UserForm()

    return render(request, 'conertainly/register.html', context = {'user_form': user_form, 'registered': registered})