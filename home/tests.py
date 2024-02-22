from django.test import TestCase, Client
from django.urls import reverse

# Create your tests here.

class IndexViewTests(TestCase):
    def setUp(self):
        # Every test needs a client.
        self.client = Client()

    def test_index_view_with_positive_x(self):
        # Test the index view with a positive 'x' value
        response = self.client.get(reverse('index'), {'x': '1'})
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'x_greater_index.html')

    def test_index_view_with_negative_x(self):
        # Test the index view with a negative 'x' value
        response = self.client.get(reverse('index'), {'x': '-1'})
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'x_lower_index.html')

    def test_index_view_with_zero_x(self):
        # Test the index view with 'x' value of zero
        response = self.client.get(reverse('index'), {'x': '0'})
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'x_lower_index.html')

    def test_index_view_without_x(self):
        # Test the index view without providing 'x' value
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'x_lower_index.html')

    def test_index_view_with_non_integer_x(self):
        # Test the index view with non-integer 'x' value
        response = self.client.get(reverse('index'), {'x': 'abc'})
        self.assertEqual(response.status_code, 404)
