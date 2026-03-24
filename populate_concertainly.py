from math import hypot
import os
from datetime import date
os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                     'wad_project.settings')


import django
django.setup()

from django.contrib.auth.models import User  # noqa: E402
from concertainly.models import Artist, Tour, Song, Review, Genre, Venue  # noqa: E402

def add_genre(name, nice_name):
    genre,_ = Genre.objects.get_or_create(name=name, nice_name=nice_name)
    return genre

def add_venue(name, city):
    venue, _ = Venue.objects.get_or_create(name=name, defaults={
        "city": city
    })
    return venue

def add_artist(name, genres, spotify_id, external_id):
    artist,_ = Artist.objects.get_or_create(
        name=name,
        defaults={
            "spotify_id": spotify_id,
            "external_id": external_id
        }
    )

    artist.genres.add(genres)
    
    changed = False

    if artist.spotify_id != spotify_id:
        artist.spotify_id = spotify_id
        changed = True

    if artist.external_id != external_id:
        artist.external_id = external_id
        changed = True
    
    if changed:
        artist.save()
        
    return artist

def add_user(name, password):
    user,created = User.objects.get_or_create(username = name)
    if created:
        user.set_password(password)
        user.save()
    return user
    
def add_tour(name, artist, ticket_master_id = "", image=""):
    tour,_ = Tour.objects.get_or_create(
        name=name, 
        artist=artist,
        defaults={"external_id": ticket_master_id, "image": image}
    )
    if tour.external_id != ticket_master_id:
        tour.external_id = ticket_master_id
        tour.save()
    return tour

def add_song(name, artist, spotify_id):
    song,_ = Song.objects.get_or_create(
        name=name, 
        artist=artist,
        defaults={"external_id": spotify_id}
    )
    if song.external_id != spotify_id:
        song.external_id = spotify_id
        song.save()
    return song

def add_review(title, thoughts, img, venue, date, rating, user, tour, songs):
    review, created = Review.objects.get_or_create(        
        title=title,
        user=user,
        tour=tour,
        defaults={
            "thoughts": thoughts,
            "img": img,
            "venue": venue,
            "date": date,
            "rating": rating,
        }
    )

    if img:
        review.img = img
    else:
        review.img = None
    review.save()
    review.set_list.set(songs)

    return review

def populate():
    pop = add_genre("pop", "Pop")
    rock = add_genre("rock","Rock")
    rb = add_genre("rnb","R&B")
    classical = add_genre("classical","Classical")
    hiphop = add_genre("hiphop","Hip-Hop")
    metal = add_genre("metal", "Metal")
    jpop = add_genre("jpop", "J-Pop")
    punk = add_genre("punk", "Punk")
    kpop = add_genre("kpop", "K-Pop")
    latin = add_genre("latin", "Latin")
    edm = add_genre("edm", "EDM")
    mandopop = add_genre("mandopop", "Mandopop")

     
    billie = add_artist("Billie Eilish", pop,  "6qqNVTkY8uBg9cP3Jd7DAH", "f4abc0b5-3f7a-4eff-8f78-ac078dbce533")
    linkin = add_artist("Linkin Park", rock, "6XyY86QOPPrYVGvF9ch6wz", "f59c5520-5f46-4d2c-b2c4-822eabf53419")
    taylor = add_artist("Taylor Swift", pop, "06HL4z0CvFAxyc27GXpf02", "20244d07-534f-4eff-b4d4-930878889970")
    harry = add_artist("Harry Styles", pop, "6KImCVD70vtIoJWnq6nGn3", "7eb1ce54-a355-41f9-8d68-e018b096d427")
    olivia = add_artist("Olivia Rodrigo", pop, "1McMsnEElThX1knmY4oliG", "6925db17-f35e-42f3-a4eb-84ee6bf5d4b0")
    sabrina = add_artist("Sabrina Carpenter", pop, "74KM79TiuVKeVCqs8QtB0B", "1882fe91-cdd9-49c9-9956-8e06a3810bd4")
    conan = add_artist("Conan Gray", pop, "4Uc8Dsxct0oMqx0P6i60ea", "1882fe91-cdd9-49c9-9956-8e06a3810bd4")
    niall = add_artist("Niall Horan", pop,"1Hsdzj7Dlq2I7tHP7501T4", "55e6074f-ef78-4ec3-8fff-bd1b8cc8c14a")
    sombr = add_artist("Sombr", pop, "4G9NDjRyZFDlJKMRL8hx3S", "502cf908-9921-48bc-bf0e-265c881c0156")
    
    charlotte = add_user("Charlotte.528", "password")
    mark = add_user("Mark420", "password")
    emma = add_user("Emma_0104", "password")
    john = add_user("John8429", "password")
    delilah = add_user("Delilah+_+", "password")
    alice = add_user("Alice-4922", "password")
    carolina = add_user("Carolina-3958", "password")
    lizzy = add_user("Lizzy@_@", "password")
    nate = add_user("Nate.-.", "password")
    luna = add_user("Luna-_-", "password")
    george = add_user("George100", "password")
    casey = add_user("Casey<3", "password")

    #one review
    hit_me_hard_and_soft = add_tour("Hit Me Hard and Soft: The Tour", billie, image="images/tour/billie.jpg")
    from_zero = add_tour("FROM ZERO World Tour", linkin, image="images/tour/linkin.jpg")
    guts = add_tour("GUTS World Tour", olivia, image="images/tour/olivia.jpg")
    superache = add_tour("Superache Tour", conan, image="images/tour/conan.jpg")
    theshow = add_tour("The Show", niall, image="images/tour/niall.jpg")
    sombr_world_tour = add_tour("Sombr World Tour", sombr, image="images/tour/sombr.jpg")


    #two reviews
    love_on_tour = add_tour("Love on Tour", harry, image="images/tour/harry.jpg")
    short_n_sweet = add_tour("Short n' Sweet", sabrina, image="images/tour/sabrina.jpeg")
    the_eras_tour = add_tour("The Eras Tour", taylor, image="images/tour/taylor.jpg")


    #no reviews
    the_eras_tour_2 = add_tour("The Eras Tour 2.0", taylor, image="images/tour/erastour2.jpg")
    fearless_tour = add_tour("Fearless Tour", taylor, image="images/tour/fearless.jpg")
    speak_now_world_tour = add_tour("Speak Now World Tour", taylor, image="images/tour/speaknow.jpg")
    the_red_tour = add_tour("The Red Tour", taylor, image="images/tour/redtour.jpg")

    billie_s1 = add_song("bad guy", billie, "2Fxmhks0bxGSBdJ92vM42m")
    billie_s2 = add_song("BIRDS OF A FEATHER", billie, "6dOtVTDdiauQNBQEDOtlAB")
    billie_s3 = add_song("CHIHIRO", billie, "7BRD7x5pt8Lqa1eGYC4dzj") 
    linkin_s1 = add_song("Numb", linkin, "2nLtzopw4rPReszdYBJU6h")
    linkin_s2 = add_song("In the End", linkin, "60a0Rd6pjrkxjPbaKzXjfq")
    linkin_s3 = add_song("Faint", linkin, "7AB0cUXnzuSlAnyHOqmrZr")
    taylor_s1 = add_song("Fearless", taylor, "77sMIMlNaSURUAXq5coCxE")
    taylor_s2 = add_song("You Belong With Me", taylor, "1GEBsLDvJGw7kviySRI6GX")
    taylor_s3 = add_song("Love Story", taylor, "1D4PL9B8gOg78jiHg3FvBb")
    harry_s1 = add_song("Kiwi", harry, "33SNO8AaciGbNaQFkxvPrW")
    harry_s2 = add_song("Only Angel", harry, "5Lbsc65org0b85kNsPkluY")
    harry_s3 = add_song("Cinema", harry, "35TyJIMR3xRouUuo2sjS6v")
    harry_s4 = add_song("Golden", harry, "45S5WTQEGOB1VHr1Q4FuPl")
    harry_s5 = add_song("Two Ghosts", harry, "4B1rpPmQXwj78wk6aIGwwU")
    harry_s6 = add_song("Lights Up", harry, "4jAIqgrPjKLTY9Gbez25Qb")
    sabrina_s1 = add_song("Busy Woman", sabrina, "0b0Dz0Gi86SVdBxYeiQcCP")
    sabrina_s2 = add_song("Juno", sabrina, "21B4gaTWnTkuSh77iWEXdS")
    sabrina_s3 = add_song("Manchild", sabrina, "42UBPzRMh5yyz0EDPr6fr1")
    sabrina_s4 = add_song("Feather", sabrina, "2Zo1PcszsT9WQ0ANntJbID")
    sabrina_s5 = add_song("Nobody's Son", sabrina, "4SRShYMtFIGgnOU7iBicMH")
    sabrina_s6 = add_song("House Tour", sabrina, "25jgQBxuUkGDdCG1WGKKN9")
    conan_s1 = add_song("This Song", conan, "2k6FKrR0wDIs6xCtU51GZ7")
    conan_s2 = add_song("Movies", conan, "6FH6fmlh9DbvssuEQyQEVd")
    conan_s3 = add_song("Actor", conan, "60mJHAb1XIDyk9bTLnyaQU")
    olivia_s1 = add_song("Lacy", olivia, "6QT6j7rKt7Vk3IuV2AUO9W")
    olivia_s2 = add_song("so american", olivia, "5Jh1i0no3vJ9u4deXkb4aV")
    olivia_s3 = add_song("love is embarrassing", olivia, "26QLJMK8G0M06sk7h7Fkse")

    ovo = add_venue("OVO Hydro", "Glasgow")
    barclays = add_venue("Barclays Center", "Brooklyn")
    murrayfield_stadium = add_venue("Murrayfield Stadium", "Edinbrugh")
    ibrox = add_venue("Ibrox Statium", "Glasgow")
    wembley = add_venue("Wembly Stadium", "London")
    coop_live = add_venue("Co-op Live", "Manchester")
    utilita_arena = add_venue("Utilita Arena", "Birmingham")
    eventim_apollo = add_venue("Eventim Apollo", "London")
    sse_arena = add_venue("SSE Arena", "Belfast")
    o2_academy_birmingham = add_venue("O2 Academy", "Birmingham")

    add_review(
        title = "Best tour forever",
        thoughts = "love itttt. Already looking forward to the next show.xxxxx",
        img = "reviews/billie_1.jpg",
        venue = ovo,
        date = date(2025,6,7),
        rating = 4,
        user = charlotte,
        tour = hit_me_hard_and_soft,
        songs = [billie_s1, billie_s2, billie_s3],
    )

    add_review(
        title = "BEST",
        thoughts = "The nostalgia... Act 4 is my favourite. Soldiers forever.",
        img = "reviews/linkin_1.jpg",
        venue = barclays,
        date = date(2024,11,16),
        rating = 5,
        user = mark,
        tour = from_zero,
        songs = [linkin_s1, linkin_s2, linkin_s3],
    )

    add_review(
        title = "<3<3<3",
        thoughts = "Everything is so good espcailly like OMG I love her sm",
        img = "reviews/taylor_1.jpg",
        venue = murrayfield_stadium ,
        date = date(2024,6,9),
        rating = 5,
        user = emma,
        tour = the_eras_tour,
        songs = [taylor_s1, taylor_s2, taylor_s3]
    )

    add_review(
        title = "Good show",
        thoughts = "I came to this concert with my daughter. I get why she loves taylor swift so much.",
        img = "",
        venue = wembley,
        date = date(2024,6,21),
        rating = 4,
        user = john,
        tour = the_eras_tour,
        songs = []
    )

    add_review(
        title = "starstruck",
        thoughts = "been a fan since the 1d days... still am",
        img = "",
        venue = ibrox,
        date = date(2022,6,11),
        rating = 5,
        user = carolina,
        tour = love_on_tour,
        songs = [harry_s4, harry_s5, harry_s6]
    )

    add_review(
        title = "fantastic show",
        thoughts = "proper performance from the vocals to the costume design to the dance choreography",
        img = "",
        venue = coop_live,
        date = date(2025,3,13),
        rating = 5,
        user = delilah,
        tour = short_n_sweet,
        songs = [sabrina_s1, sabrina_s2, sabrina_s3]
    )

    add_review(
        title = "sweeeet",
        thoughts = "luved it!",
        img = "",
        venue = utilita_arena,
        date = date(2025,3,6),
        rating = 4,
        user = alice,
        tour = short_n_sweet,
        songs = [sabrina_s4, sabrina_s5, sabrina_s6]
    )

    add_review(
        title = ":D",
        thoughts = "absolutely brilliant",
        img = "",
        venue = wembley,
        date = date(2023,6,13),
        rating = 4,
        user = nate,
        tour = love_on_tour,
        songs = [harry_s1, harry_s2, harry_s3]
    )

    add_review(
        title = "get tickets!",
        thoughts = "so good, already have tickets to see his next tour WishBone World Tour",
        img = "",
        venue = eventim_apollo,
        date = date(2022,6,9),
        rating = 5,
        user = lizzy,
        tour = superache,
        songs = [conan_s1, conan_s2, conan_s3]
    )

    add_review(
        title = "did not disapoint at all!",
        thoughts = "after listening to this album so much in my bedroom it was cool to hear it live",
        img = "",
        venue = ovo,
        date = date(2024,5,7),
        rating = 4,
        user = luna,
        tour = guts,
        songs = [olivia_s1, olivia_s2, olivia_s3]
    )

    add_review(
        title = "the show!",
        thoughts = "great show (pardon the pun haha)",
        img = "",
        venue = sse_arena,
        date = date(2024,2,21),
        rating = 4,
        user = george,
        tour = theshow,
        songs = []
    )

    add_review(
        title = "impressed",
        thoughts = "officially a new fan after this - get on the sombr train if you havent yet!!",
        img = "",
        venue = o2_academy_birmingham,
        date = date(2026,3,13),
        rating = 4,
        user = casey,
        tour = sombr_world_tour,
        songs = []
    )

    

if __name__ == '__main__':
    print('Starting concert-ainly population script...')
    populate()
