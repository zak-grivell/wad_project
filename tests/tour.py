from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from concertainly.models import Tour, Review, Artist, Genre
from datetime import date

class ShowReviewTest(TestCase):
    def setUp(self):
        User = get_user_model()
        self.user = User.objects.create_user(
            username="testuser",
            password="password"
        )

        self.genre = Genre.objects.create(name = "pop")

        self.artist = Artist.objects.create(
            name = "Test Artist",
            spotify_id = "testid123456789",
            genre = self.genre,
            slug = "test-artist",
        )

        self.tour_1 = Tour.objects.create(
            name = "Test Tour",
            slug = "test-tour",
            artist = self.artist
        )

        self.tour_2 = Tour.objects.create(
            name = "Other Tour",
            slug = "other-tour",
            artist = self.artist
        )

        self.review_1 = Review.objects.create(
            tour = self.tour_1,
            user = self.user,
            title = "Testing Review",
            thoughts = "some random text to show it works.",
            city = "Glasgow",
            venue = "OVO Hydro",
            date = date(2024,6,21),
            rating = 1
        )

        self.review_2 = Review.objects.create(
            tour=self.tour_1,
            user=self.user,
            title="Testing Review 2",
            thoughts="another review",
            city="Manchester",
            venue="AO Arena",
            date=date(2024,6,22),
            rating=4
        )


    def test_with_review(self):
        response = self.client.get(
            reverse("concertainly:tour", args=[self.tour_1.slug])
        )

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "tour.html")
        self.assertContains(response, "Testing Review")
        self.assertContains(response, "some random text to show it works.")
        self.assertContains(response, "Glasgow")
        self.assertContains(response, "OVO Hydro")
        self.assertContains(response, "2024")

    def test_with_no_review(self):
        Review.objects.filter(tour = self.tour_1).delete()
        response = self.client.get(
            reverse("concertainly:tour", args=[self.tour_1.slug])
        )
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Be the first one to comment for this tour!")

    def test_with_invalid_tour(self):
        response = self.client.get(
            reverse("concertainly:tour", args=["not-existed-slug"])
        )
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Tour Not Found")

    def test_with_filtered_tour(self):
        Review.objects.create(
            tour = self.tour_2,
            user = self.user,
            title = "Should not exist",
            thoughts = "some random text",
            city = "Glasgow",
            venue = "OVO Hydro",
            date = date(2024,6,21),
            rating = 1
        )

        response = self.client.get(reverse("concertainly:tour", args=[self.tour_1.slug]))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Testing Review")
        self.assertContains(response, "Testing Review 2")
        self.assertNotContains(response, "Should not exist")

    def test_with_display_multi_reviews(self):
        response = self.client.get(reverse("concertainly:tour", args=[self.tour_1.slug]))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Testing Review")
        self.assertContains(response, "Testing Review 2")