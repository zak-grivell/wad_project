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
     
    billie = add_artist("Billie Eilish", "spotify_billie_eilish")
    linkin = add_artist("Linkin Park", "spotify_linkin_park")
    taylor = add_artist("Taylor Swift", "spotify_taylor_swift")
    
    charlotte = add_user("Charlotte", "password")
    mark = add_user("Mark", "password")
    emma = add_user("Emma", "password")
    john = add_user("John", "password")

    #one review
    hit_me_hard_and_soft = add_tour("Hit Me Hard and Soft: The Tour", billie)
    from_zero = add_tour("FROM ZERO World Tour", linkin)
    #two reviews
    the_eras_tour = add_tour("The Eras Tour", taylor)
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
    

if __name__ == '__main__':
    print('Starting concert-ainly population script...')
    populate()