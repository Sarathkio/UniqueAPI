from django.test import TestCase, Client
from django.urls import reverse
import json

class APITestCase(TestCase):
    def setUp(self):
        # Initialize the test database or create mock objects if necessary
        pass

    def test_get_all_data(self):
        # Test the /api/data/ endpoint (GET request)
        response = self.client.get(reverse('api:data-list'))
        self.assertEqual(response.status_code, 200)

    def test_merge_data_valid_input(self):
        # Test the /api/merge/ endpoint with valid input data
        data = [{'name': 'John', 'age': 25, 'email': 'john@example.com'}]
        response = self.client.post(reverse('api:merge-list'), json.dumps(data), content_type='application/json')
        self.assertEqual(response.status_code, 200)

    def test_merge_data_invalid_input(self):
        # Test the /api/merge/ endpoint with invalid input data
        invalid_data = [{'name': 'John', 'age': 25}]  # Missing 'email' field
        response = self.client.post(reverse('api:merge-list'), json.dumps(invalid_data), content_type='application/json')
        self.assertEqual(response.status_code, 400)

        def test_merge_data_missing_field(self):
            # Test the /api/merge/ endpoint with missing fields in input data
            invalid_data = [{'name': 'John', 'age': 25}]  # Missing 'email' field
            response = self.client.post(reverse('api:merge-list'), json.dumps(invalid_data),
                                        content_type='application/json')
            self.assertEqual(response.status_code, 400)
            self.assertIn('email',
                          response.json()['message'])  # Check if the error message contains the missing field name

        def test_merge_data_invalid_age(self):
            # Test the /api/merge/ endpoint with invalid 'age' field in input data
            invalid_data = [{'name': 'John', 'age': -25, 'email': 'john@example.com'}]  # Negative age
            response = self.client.post(reverse('api:merge-list'), json.dumps(invalid_data),
                                        content_type='application/json')
            self.assertEqual(response.status_code, 400)
            self.assertIn('age', response.json()['message'])  # Check if the error message contains the 'age' field

        def test_merge_data_invalid_email(self):
            # Test the /api/merge/ endpoint with invalid 'email' field in input data
            invalid_data = [{'name': 'John', 'age': 25, 'email': 'invalid_email'}]  # Invalid email format
            response = self.client.post(reverse('api:merge-list'), json.dumps(invalid_data),
                                        content_type='application/json')
            self.assertEqual(response.status_code, 400)
            self.assertIn('email', response.json()['message'])  # Check if the error message contains the 'email' field

        def test_merge_data_empty_payload(self):
            # Test the /api/merge/ endpoint with an empty JSON payload
            response = self.client.post(reverse('api:merge-list'), '{}', content_type='application/json')
            self.assertEqual(response.status_code, 400)
            self.assertIn('Invalid JSON payload', response.json()['message'])