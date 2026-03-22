import os
from datetime import date
os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                     'wad_project.settings')

import django
django.setup()
from django.contrib.auth.models import User
from concertainly.models import Artist, Tour, Song, Review, Genre

def add_genre(name):
    genre,_ = Genre.objects.get_or_create(name=name)
    return genre

def add_artist(name, spotify_id):
    artist,_ = Artist.objects.get_or_create(
        name=name,
        defaults={"spotify_id": spotify_id}
        )
    if artist.spotify_id != spotify_id:
        artist.spotify_id = spotify_id
        artist.save()
    return artist

def add_user(name, password):
    user,created = User.objects.get_or_create(username = name)
    if created:
        user.set_password(password)
        user.save()
    return user
    
def add_tour(name, artist, ticket_master_id = ""):
    tour,_ = Tour.objects.get_or_create(
        name=name, 
        artist=artist,
        defaults={"ticket_master_id": ticket_master_id}
    )
    if tour.ticket_master_id != ticket_master_id:
        tour.ticket_master_id = ticket_master_id
        tour.save()
    return tour

def add_song(name, artist, spotify_id):
    song,_ = Song.objects.get_or_create(
        name=name, 
        artist=artist,
        defaults={"spotify_id": spotify_id}
    )
    if song.spotify_id != spotify_id:
        song.spotify_id = spotify_id
        song.save()
    return song

def add_review(title, thoughts, img, city, venue, date, rating, user, tour, songs):
    review, created = Review.objects.get_or_create(        
        title=title,
        user=user,
        tour=tour,
        defaults={
            "thoughts": thoughts,
            "img": img,
            "city": city,
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
    add_genre("Rock")
    add_genre("Pop")
     
    billie = add_artist("Billie Eilish", "6qqNVTkY8uBg9cP3Jd7DAH")
    linkin = add_artist("Linkin Park", "6XyY86QOPPrYVGvF9ch6wz")
    taylor = add_artist("Taylor Swift", "06HL4z0CvFAxyc27GXpf02")
    harry = add_artist("Harry Styles", "6KImCVD70vtIoJWnq6nGn3")
    olivia = add_artist("Olivia Rodrigo","1McMsnEElThX1knmY4oliG")
    sabrina = add_artist("Sabrina Carpenter","74KM79TiuVKeVCqs8QtB0B")
    conan = add_artist("Conan Gray", "4Uc8Dsxct0oMqx0P6i60ea")
    
    charlotte = add_user("Charlotte", "password")
    mark = add_user("Mark", "password")
    emma = add_user("Emma", "password")
    john = add_user("John", "password")
    delilah = add_user("Delilah", "password")
    alice = add_user("Alice", "password")
    carolina = add_user("Carolina", "password")
    lizzy = add_user("Lizzy", "password")
    nate = add_user("Nate", "password")
    luna = add_user("Luna", "password")

    #one review
    hit_me_hard_and_soft = add_tour("Hit Me Hard and Soft: The Tour", billie)
    from_zero = add_tour("FROM ZERO World Tour", linkin)
    guts = add_tour("GUTS World Tour", olivia)
    superache = add_tour("Superache Tour", conan)

    #two reviews
    the_eras_tour = add_tour("The Eras Tour", taylor)
    love_on_tour = add_tour("Love on Tour", harry)
    short_n_sweet = add_tour("Short n' Sweet", sabrina)


    #no reviews
    the_eras_tour_2 = add_tour("The Eras Tour 2.0", taylor)
    fearless_tour = add_tour("Fearless Tour", taylor)
    speak_now_world_tour = add_tour("Speak Now World Tour", taylor)
    the_red_tour = add_tour("The Red Tour", taylor)

    billie_s1 = add_song("bad guy", billie, "spotify_bad_guy")
    billie_s2 = add_song("BIRDS OF A FEATHER", billie, "spotify_birds_of_a_feather")
    billie_s3 = add_song("CHIHIRO", billie, "spotify_chihiro") 
    linkin_s1 = add_song("Numb", linkin, "spotify_numb")
    linkin_s2 = add_song("In the End", linkin, "spotify_in_the_end")
    linkin_s3 = add_song("Faint", linkin, "spotify_faint")
    taylor_s1 = add_song("Fearless", taylor, "spotify_fearless")
    taylor_s2 = add_song("You Belong With Me", taylor, "spotify_you_belong_with_me")
    taylor_s3 = add_song("Love Story", taylor, "spotify_love_story")
    harry_s1 = add_song("Kiwi", harry, "spotify_kiwi")
    harry_s2 = add_song("Only Angel", harry, "spotify_only_angel")
    harry_s3 = add_song("Cinema", harry, "spotify_cinema")
    harry_s4 = add_song("Golden", harry, "spotify_golden")
    harry_s5 = add_song("Two Ghosts", harry, "spotify_two_ghosts")
    harry_s6 = add_song("Lights Up", harry, "spotify_lights_up")
    sabrina_s1 = add_song("Busy Woman", sabrina, "spotify_busy_woman")
    sabrina_s2 = add_song("Juno", sabrina, "spotify_juno")
    sabrina_s3 = add_song("Manchild", sabrina, "spotify_manchild")
    sabrina_s4 = add_song("Feather", sabrina, "spotify_feather")
    sabrina_s5 = add_song("Nobody's Son", sabrina, "spotify_nobodys_son")
    sabrina_s6 = add_song("House Tour", sabrina, "spotify_house_tour")
    conan_s1 = add_song("This Song", conan, "spotify_this_song")
    conan_s2 = add_song("Movies", conan, "spotify_movies")
    conan_s3 = add_song("Actor", conan, "spotify_actor")
    olivia_s1 = add_song("Lacy", olivia, "spotify_lacy")
    olivia_s2 = add_song("so american", olivia, "spotify_so_american")
    olivia_s3 = add_song("love is embarrassing", olivia, "spotify_love_is_embarrassing")

    add_review(
        title = "Best tour forever",
        thoughts = "love itttt. Already looking forward to the next show.xxxxx",
        img = "reviews/billie_1.jpg",
        city = "Glasgow",
        venue = "OVO Hydro",
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
        city = "Brooklyn",
        venue = "Barclays Center",
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
        city = "Edinburgh",
        venue = "Murrayfield Stadium",
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
        city = "London",
        venue = "Wembley Stadium",
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
        city = "Glasgow",
        venue = "Ibrox Stadium",
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
        city = "Manchester",
        venue = "Co-op Live",
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
        city = "Birmingham",
        venue = "Utilita Arena",
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
        city = "London",
        venue = "Wembly Stadium",
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
        city = "London",
        venue = "Eventim Opollo",
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
        city = "Glasgow",
        venue = "Ovo Hydro",
        date = date(2024,5,7),
        rating = 4,
        user = luna,
        tour = guts,
        songs = [olivia_s1, olivia_s2, olivia_s3]
    )
    

if __name__ == '__main__':
    print('Starting concert-ainly population script...')
    populate()
