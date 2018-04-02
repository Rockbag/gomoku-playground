import json
from unittest.mock import patch

from django.contrib.auth.models import User
from django.test import TestCase, Client


class UserRegistrationTestCase(TestCase):

    def setUp(self):
        self.client = Client()

    def tearDown(self):
        User.objects.all().delete()

    def test_user_is_created(self):
        self.client.post('/user/register/', data={'username': 'john.doe@test.com', 'password': 'test1234'})
        u = User.objects.get_by_natural_key('john.doe@test.com')
        self.assertIsNotNone(u)

    @patch('backend.api.user.views.User.objects.create_user', side_effect=Exception())
    def test_error_is_shown(self, create_user):
        expected_reponse_data = {'status': 'error',
                                 'error_message': 'Unexpected error while creating user'}

        response = self.client.post('/user/register/', data={'username': 'john.doe@test.com', 'password': 'test1234'})
        self.assertDictEqual(expected_reponse_data, json.loads(response.content))
