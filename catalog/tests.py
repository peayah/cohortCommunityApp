from django.test import SimpleTestCase
from django.urls import reverse


class IndexPageTests(SimpleTestCase):

    def test_url_exists_at_correct_location(self):
        response = self.client.get("/catalog/")
        self.assertEqual(response.status_code, 200)

    def test_url_available_by_name(self):
        response = self.client.get(reverse("index"))
        self.assertEqual(response.status_code, 200)

    def test_template_name_correct(self):  # new
        response = self.client.get(reverse("index"))
        self.assertTemplateUsed(response, "index.html")

    def test_template_content(self):
        response = self.client.get(reverse("index"))
        self.assertContains(response, "<h1>Cohorts</h1>")


class AboutPageTests(SimpleTestCase):
    def test_url_exists_at_correct_location(self):
        response = self.client.get("/catalog/about/")
        self.assertEqual(response.status_code, 200)

    def test_url_available_by_name(self):
        response = self.client.get(reverse("about"))
        self.assertEqual(response.status_code, 200)

    def test_template_name_correct(self):  # new
        response = self.client.get(reverse("about"))
        self.assertTemplateUsed(response, "about.html")

    def test_template_content(self):  # new
        response = self.client.get(reverse("about"))
        self.assertContains(response, "<h1>About</h1>")


class EventsPageTests(SimpleTestCase):
    def test_url_exists_at_correct_location(self):
        response = self.client.get("/catalog/events/")
        self.assertEqual(response.status_code, 200)

    def test_url_available_by_name(self):
        response = self.client.get(reverse("events"))
        self.assertEqual(response.status_code, 200)

    def test_template_name_correct(self):
        response = self.client.get(reverse("events"))
        self.assertTemplateUsed(response, "events.html")

    def test_template_content(self):
        response = self.client.get(reverse("events"))
        self.assertContains(response, "<h1>Upcoming Cohort Events</h1>")

