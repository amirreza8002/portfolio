from django.test import SimpleTestCase
from django.urls import reverse


class TestHomePage(SimpleTestCase):

    def test_page_available(self):
        response = self.client.get(reverse("home"))

        assert response.status_code == 200

    def test_template_used(self):
        response = self.client.get(reverse("home"))
        self.assertTemplateUsed(response, "pages/home.html")

    def test_template_content(self):
        response = self.client.get(reverse("home"))
        self.assertContains(response, "Home")


class TestAboutPage(SimpleTestCase):
    def test_available(self):
        response = self.client.get(reverse("about"))
        assert response.status_code == 200

    def test_template_used(self):
        response = self.client.get(reverse("about"))
        self.assertTemplateUsed(response, "pages/about.html")

    def test_template_content(self):
        response = self.client.get(reverse("about"))
        self.assertContains(response, "About")
