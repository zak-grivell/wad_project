from django.test import TestCase
from django.conf import settings
import os
from django.urls import reverse
from populate_concertainly import populate

class BaseTemplate(TestCase):

    def get_template(self, path_to_template):

        f = open(path_to_template, 'r')
        template_str = ""

        for line in f:
            template_str = f"{template_str}{line}"

        f.close()
        return template_str

    def test_nav_bar_works(self):
        base_template = self.get_template(os.path.join(settings.TEMPLATE_DIR,'base.html'))
        nav_bar_needs = [
            'href="{% url \'concertainly:home\' %}"',
            'href="{% url \'concertainly:genres\' %}"',
            'href="{% url \'concertainly:login\' %}"',
            'href="{% url \'concertainly:register\' %}"',
        ]
        for link in nav_bar_needs:
            self.assertTrue(link in base_template)

    def test_all_templates_use_base(self):
        uses_base = "{% extends 'base.html' %}"
        templates = ['artist.html',
                     'homepage.html',
                     'genre.html',
                     'allGenres.html',
                     'login.html',
                     'register.html',
                     'tour.html',
                     ]
        for t in templates:
            template = self.get_template(os.path.join(settings.TEMPLATE_DIR,t))
            self.assertTrue(uses_base in template)


class HomePage(TestCase):

    def test_page_loads(self):
        populate()
        response = self.client.get(reverse('concertainly:home'))
        self.assertEqual(response.status_code, 200)

    def test_homepage_displays_highlight_tour(self):
        populate()
        response = self.client.get(reverse('concertainly:home'))
        self.assertIn('highlight_tour', response.context)

    def test_homepage_displays_popular_tours(self):
        populate()
        response = self.client.get(reverse('concertainly:home'))
        self.assertIn('popular_tours', response.context)


class ArtistPage(TestCase):

    def test_example_artist(self):
        populate()
        response = self.client.get(reverse('concertainly:artist', kwargs={'slug': 'taylor-swift'}))
        self.assertEqual(response.status_code, 200)

class GenrePage(TestCase):

    def test_example_genre(self):
        populate()
        response = self.client.get(reverse('concertainly:genre', kwargs={'genre_name': 'pop'}))
        self.assertEqual(response.status_code, 200)

class LoginPage(TestCase):

    def test_username_field(self):
        response = self.client.get(reverse('concertainly:login'))
        self.assertContains(response, "Username: <input type=\"text\" name=\"username\" value=\"\"")

    def test_password_field(self):
        response = self.client.get(reverse('concertainly:login'))
        self.assertContains(response, "Password: <input type=\"password\" name=\"password\" value=\"\"")