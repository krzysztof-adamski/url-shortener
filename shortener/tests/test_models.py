from django.conf import settings
from django.test import TestCase

from shortener.models import Shortcut


class ShortcutModelTests(TestCase):
    def setUp(self):
        self.url = "http://wp.pl"
        self.link = "wppl"
        Shortcut.objects.create(url=self.url, link=self.link)

    def test_should_create_shortcut(self):
        """Shortcut should be created."""
        shortcut = Shortcut.objects.get(url=self.url)
        self.assertEqual(shortcut.url, self.url)

    def test_shortcut_str(self):
        """Shortcut object str."""
        shortcut = Shortcut.objects.get(url=self.url)
        self.assertEqual(shortcut.__str__(), self.url)

    def test_shortcut_absolute_url(self):
        """Shortcut object absolute url."""
        shortcut = Shortcut.objects.get(url=self.url)
        self.assertEqual(shortcut.get_absolute_url(), f"/{self.link}/")

    def test_shortcut_link_url(self):
        """Shortcut object link url."""
        shortcut = Shortcut.objects.get(url=self.url)
        expected_url = f"{settings.BASE_URL}/{self.link}"
        self.assertEqual(shortcut.get_link_url, expected_url)
