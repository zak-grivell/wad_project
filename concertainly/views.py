from django.shortcuts import render, get_object_or_404
from concertainly.models import Genre, Artist, Tour, Review, Venue, Song
from concertainly.forms import UserForm, ReviewForm, SearchForm
from django.shortcuts import redirect 
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db.models import Count

def home(request):
    tours = (
        Tour.objects.annotate(review_count=Count("review"))
        .filter(review_count__gt=0)
        .order_by("-review_count")
    )

    highlight_tour = tours[0:3]
    popular_tours = tours [3:13]

    context_dict = {}

    if len(highlight_tour) == 0:
        return error_page(request, context_dict, "We had some trouble loading the data - none was found!")
    
    tour1 = highlight_tour[0]
    tour2 = highlight_tour[1]
    tour3 = highlight_tour[2]

    
    context_dict["highlight_tour"] = highlight_tour
    context_dict["popular_tours"] = popular_tours
    context_dict["tour1"] = tour1
    context_dict["tour2"] = tour2
    context_dict["tour3"] = tour3

    return render(request, "homepage.html", context=context_dict)

def insens_str_contain(s1, s2):
    return (s1.lower() in s2.lower() or s2.lower() in s1.lower())

def contained_in_any_list_elt(target, list):
    for elt in list:
        if target in elt:
            return True
    return False

def search(request):
    form_dict_key = "form"
    if (request.method == "POST"):
        form = SearchForm(request.POST, request.FILES)

        if form.is_valid():
            clean_artist = str(form.cleaned_data["artist_select"])
            clean_tour = str(form.cleaned_data["tour_select"])
            clean_venue = str(form.cleaned_data["venue_select"])
            s_date=form.cleaned_data["date"],
            clean_genre = str(form.cleaned_data["genre_select"])

            # me when i query every single object in the database
            # if it lags i'll fix it
            # premature optimisation is the root of all evil
            reviews = Review.objects.all()
            context_dict = {}

            # collect all presence bools - if all are false, display an error message
            presences = []

            artist_present = clean_artist != ""
            presences.append(artist_present)
            if (artist_present):
                reviews = [r for r in reviews if insens_str_contain(r.artist().name, clean_artist)]
                context_dict["search_artist"] = clean_artist

            tour_present = clean_tour != ""
            presences.append(tour_present)
            if (tour_present):
                reviews = [r for r in reviews if insens_str_contain(clean_tour, r.tour.name)]
                context_dict["search_tour"] = clean_tour

            venue_present = clean_venue != ""
            presences.append(venue_present)
            if (venue_present):
                reviews = [r for r in reviews if insens_str_contain(clean_venue, r.venue.name)]
                context_dict["search_venue"] = clean_venue

            if (s_date is not None and s_date[0] is not None):
                presences.append(True)
                formatted_date = s_date[0].strftime('%Y-%m-%d')
                reviews = [r for r in reviews if r.date.strftime('%Y-%m-%d') == formatted_date]
                context_dict["search_date"] = s_date[0].strftime('%d-%m-%Y')
            else:
                presences.append(False)

            presences.append(bool(clean_genre))
            if (clean_genre):
                reviews = [r for r in reviews if contained_in_any_list_elt(clean_genre, r.genre_name_list()) or contained_in_any_list_elt(clean_genre, r.genre_nice_name_list())]
                context_dict["search_genre"] = clean_genre

            # if there are no true presences
            if (not any(presences)):
                context_dict["error"] = "Please provide some search parameters."
                context_dict[form_dict_key] = SearchForm()
                return render(request, "search.html", context=context_dict)
                
            context_dict["reviews"] = reviews
            context_dict["number_of_reviews"] = len(reviews)
            context_dict["any_results"] = len(reviews) != 0
            return render(request, "search_results.html", context=context_dict)
        
        else:
            print("form data not valid")
            print(form.errors)
    else:
        form = SearchForm()
    
    return render(request, "search.html", {form_dict_key: form})

def search_results(request):
    return render(request, "search_results.html", dict())

def user_register(request):
    if request.user.is_authenticated:
        return redirect(reverse("concertainly:home"))
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
            if user:
                login(request, user)
            return redirect('concertainly:home')
        else:
            # if invalid, complain to the terminal
            print(user_form.errors)
            
    else:
        print("not post")
        user_form = UserForm()

    return render(request, 'register.html', context = {'user_form': user_form, 'registered': registered})

def user_login(request):
    context_dict = {}
    if request.user.is_authenticated:
        return redirect(reverse("concertainly:home"))
    
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                return redirect(reverse("concertainly:home"))
            else:
                context_dict["error"] = "Your Concertainly account is disabled."
        else:
            context_dict["error"] = "Login details invalid."

    return render(request, "login.html", context_dict)

@login_required
def user_logout(request):
    logout(request)
    return redirect(reverse("concertainly:home"))

@login_required
def account(request):
    return render(request, "account.html")

def genre_list(request):
    genreObjects = Genre.objects.all()
    genres = [
        'pop', 'rnb', 'hiphop', 'rock',
        'metal', 'classical', 'jpop', 'punk',
        'kpop', 'latin', 'edm', 'mandopop'
    ]

    return render(request, "allGenres.html", {"genres": genres})

def genre(request, genre_name):
    genre = get_object_or_404(Genre, name=genre_name)
    artists = Artist.objects.filter(genres=genre)
    context_dict = {}
    context_dict["artists"] = artists
    context_dict["genre"] = genre
    return render(request, "genre.html", context=context_dict)

def artist(request, slug):
    artist = get_object_or_404(Artist, slug=slug)
    tours = Tour.objects.filter(artist=artist)
    genre = artist.genres.first()
    context_dict = {}
    context_dict["artist"] = artist
    context_dict["tours"] = tours
    context_dict["genre"] = genre.name
    return render(request, "artist.html", context=context_dict)

def tour(request, slug):
    tour = Tour.objects.filter(slug=slug).first()
    if tour:
        reviews = Review.objects.filter(tour=tour)
        request.session["last_tour"] = tour.slug
    else:
        reviews = []
    return render(request, "tour.html", {"tour": tour, "reviews": reviews})

def tour_redirect(request):
    print("Redirect last_tour:", request.session.get("last_tour"))

    last_tour = request.session.get("last_tour")
    if last_tour:
        return redirect("concertainly:tour", slug=last_tour)
    return redirect("concertainly:home")

@login_required
def review(request, slug=None):
    if (request.method == "POST"):
        submitted_ids = request.POST.getlist('setlist')

        form = ReviewForm(request.POST, request.FILES)

        form.fields["setlist"].disabled = False
        form.fields["tour_select"].disabled = False

        setlist = [(i.split("|")[0], i.split("|")[1]) for i in submitted_ids]

        form.fields['setlist'].choices = [(i, i) for i in submitted_ids]

        
        if form.is_valid():
            artist = Artist.objects.get_or_create_from_api(form.cleaned_data["artist_id"])
            tour = Tour.objects.get_or_create_from_api(form.cleaned_data["tour_id"], artist)
            venue = Venue.objects.get_or_create_from_api(form.cleaned_data["venue_id"])

            print(form.cleaned_data["setlist"])
                        
            review = Review.objects.create(
                title=form.cleaned_data["title"],
                thoughts=form.cleaned_data["comment"],
                date=form.cleaned_data["date"],
                rating=form.cleaned_data["rating"],
                img=form.cleaned_data["review_photo"],
                tour=tour,
                venue=venue,
                user=request.user
            )

            review.set_list.add(*[Song.objects.get_or_create(external_id=id, defaults={'name': name, 'artist': artist})[0] for id, name in setlist])
            

            return redirect(reverse("concertainly:tour", kwargs={"slug": tour.slug}))
        else:    
            form.fields['setlist'].choices = [(i.split("|")[0], i.split("|")[0]) for i in submitted_ids]
            print(form.errors)
    elif slug and (tour := Tour.objects.filter(slug=slug).first()):
        print("filling in")
        form = ReviewForm(initial={
          "artist_id": tour.artist.external_id,
          "artist_select": tour.artist.name,
          "tour_id": tour.external_id,
          "tour_select": tour.name
      })

        form.fields["setlist"].disabled = False
        form.fields["tour_select"].disabled = False
        
        print(f"Form initial data: {form.initial}")
    else:
        form = ReviewForm()
    
    return render(request, "review.html", {"form": form})

def error_page(request, context_dict, err_message):
    context_dict["error_message"] = err_message
    return render(request, "errorPage.html", context=context_dict)
