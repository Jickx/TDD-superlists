from django.test import TestCase
from django.http import HttpRequest
from lists.views import home_page


class TestHomePage(TestCase):
    def test_home_page_valid(self):
        response = home_page(HttpRequest())
        html = response.content.decode('utf8')

        self.assertIn('<title>To-Do list</title>', html)
        self.assertTrue(html.startswith('<html>'))
        self.assertTrue(html.endswith('</html>'))
