from unittest.mock import patch

from django.conf import settings
from django.test import Client, TestCase

from shortener.factories import ShortcutFactory
from shortener.forms import ShortcutForm
from shortener.utils import generate_shortcut


class IndexViewsTests(TestCase):
    def setUp(self):
        self.shortcut = ShortcutFactory()
        self.client = Client()

    def test_should_return_empty_form(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertTrue(isinstance(response.context["form"], ShortcutForm))
        self.assertIsNone(response.context["widget"]["value"])
        self.assertIsNone(response.context["shortcut"])

    def test_should_301_redirect_to_self(self):
        shortcut = self.shortcut
        response = self.client.get(f"/{shortcut.link}")
        self.assertEqual(response.status_code, 301)
        self.assertEqual(response.url, f"{shortcut.get_absolute_url()}")

    def test_should_302_redirect_to_external_url(self):
        shortcut = self.shortcut
        response = self.client.get(f"/{shortcut.link}/")
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, f"{shortcut.url}")

    def test_should_return_404_if_no_shortcut(self):
        response = self.client.get("/jncr7n/")
        self.assertEqual(response.status_code, 404)

    def test_should_return_400_if_no_data(self):
        response = self.client.post("/", {})
        self.assertEqual(response.status_code, 400)

    def test_should_return_400_if_no_url(self):
        response = self.client.post("/", {"cos": "innego"})
        self.assertEqual(response.status_code, 400)
        self.assertInHTML("This field is required.", response.content.decode())

    def test_should_return_400_if_wrong_url(self):
        response = self.client.post("/", {"url": "http://sfsdfsf"})
        self.assertEqual(response.status_code, 400)
        self.assertInHTML("Enter a valid URL.", response.content.decode())

    def test_should_return_400_if_too_long_url(self):
        token = generate_shortcut(lenght=3000)
        url = f"{settings.BASE_URL}/{token}"
        response = self.client.post("/", {"url": url})
        self.assertEqual(response.status_code, 400)
        self.assertInHTML(
            f"Ensure this value has at most {settings.URL_LENGHT} characters (it has {len(url)}).",
            response.content.decode(),
        )

    def test_should_return_200_and_got_shortcut(self):
        response = self.client.post("/", {"url": self.shortcut.url})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context["shortcut"].link, self.shortcut.link)
        self.assertInHTML(
            self.shortcut.get_link_url, response.content.decode()
        )

    def test_should_return_200_and_got_new_shortcut(self):
        response = self.client.post("/", {"url": "http://wp.pl"})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(str(response.context["shortcut"]), "http://wp.pl")

    @patch("shortener.utils.Shortcut")
    def test_should_return_200_and_got_new_regenerated_shortcut(
        self, mock_shortcut
    ):
        mock_shortcut.return_value.filter.return_value.exists = True
        with self.assertRaises(RecursionError) as error:
            self.client.post("/", {"url": "http://onet.pl"})
        self.assertEqual(
            error.exception.args[0],
            "maximum recursion depth exceeded in comparison",
        )
