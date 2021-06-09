import pytest
import unittest
from django.test import Client as TestClient
from rest_framework.reverse import reverse


@pytest.mark.django_db
class AuthCollection(unittest.TestCase):

    def setUp(self):
        self.client = TestClient()

    def test_get_access_token(self):
        uri = reverse('custom_token', args=())
        request_data = {
            'client_id': '4kO1VmPm5KTSApHnKQqXXXXXXXXXX',
            'client_secret': 'wnGXZQ9X8M3TENXsMbVJ018qPPLy1EOMSs5y5AgCFXXXXXXXXXXXXXX',
            'username': 'test@prudent.ai',
            'password': 'abc@12345',
            'grant_type': 'password'
        }
        response = self.client.post(uri, data=request_data)
        assert response.status_code == 200
        assert 'access_token' in response.json()['data'].keys()
        assert response.json()['success'] is True

    def test_get_access_token_with_wrong_credentials(self):
        uri = reverse('custom_token', args=())
        request_data = {
            'client_id': '4kO1VmPm5KTSApHnKQqXXXXXXXXXX',
            'client_secret': 'wnGXZQ9X8M3TENXsMbVJ018qPPLy1EOMSs5y5AgCFXXXXXXXXXXXXXX',
            'username': 'test@prudent.ai',
            'password': 'abc@123456',
            'grant_type': 'password'
        }
        response = self.client.post(uri, data=request_data)
        assert response.status_code == 422
        assert response.json()['errors'] == ['Username or Password is incorrect']
        assert response.json()['success'] is False

    def test_get_new_access_token_with_refresh_token(self):
        uri = reverse('custom_token', args=())
        request_data = {
            'client_id': '4kO1VmPm5KTSApHnKQqXXXXXXXXXX',
            'client_secret': 'wnGXZQ9X8M3TENXsMbVJ018qPPLy1EOMSs5y5AgCFXXXXXXXXXXXXXX',
            'username': 'test@prudent.ai',
            'password': 'abc@12345',
            'grant_type': 'password'
        }
        response = self.client.post(uri, data=request_data)
        request_data = {
            'client_id': '4kO1VmPm5KTSApHnKQqXXXXXXXXXX',
            'client_secret': 'wnGXZQ9X8M3TENXsMbVJ018qPPLy1EOMSs5y5AgCFXXXXXXXXXXXXXX',
            'refresh_token': response.json()['data']['refresh_token'],
            'grant_type': 'refresh_token',
        }
        response = self.client.post(uri, data=request_data)
        assert response.status_code == 200
        assert 'access_token' in response.json()['data'].keys()
        assert response.json()['success'] is True

    def test_get_new_access_token_with_tampered_refresh_token(self):
        uri = reverse('custom_token', args=())
        request_data = {
            'client_id': '4kO1VmPm5KTSApHnKQqXXXXXXXXXX',
            'client_secret': 'wnGXZQ9X8M3TENXsMbVJ018qPPLy1EOMSs5y5AgCFXXXXXXXXXXXXXX',
            'username': 'test@prudent.ai',
            'password': 'abc@12345',
            'grant_type': 'password'
        }
        response = self.client.post(uri, data=request_data)
        request_data = {
            'client_id': '4kO1VmPm5KTSApHnKQqXXXXXXXXXX',
            'client_secret': 'wnGXZQ9X8M3TENXsMbVJ018qPPLy1EOMSs5y5AgCFXXXXXXXXXXXXXX',
            'refresh_token': response.json()['data']['refresh_token'] + '123',
            'grant_type': 'refresh_token',
            'username': 'test@prudent.ai',
        }
        response = self.client.post(uri, data=request_data)
        assert response.status_code == 422
        assert response.json()['errors'] == ['Username or Password is incorrect']
        assert response.json()['success'] is False

    def test_revoke_access_token(self):
        uri = reverse('custom_token', args=())
        request_data = {
            'client_id': '4kO1VmPm5KTSApHnKQqXXXXXXXXXX',
            'client_secret': 'wnGXZQ9X8M3TENXsMbVJ018qPPLy1EOMSs5y5AgCFXXXXXXXXXXXXXX',
            'username': 'test@prudent.ai',
            'password': 'abc@12345',
            'grant_type': 'password'
        }
        response = self.client.post(uri, data=request_data)
        uri = reverse('custom_revoke_token', args=())
        request_data = {
            'client_id': '4kO1VmPm5KTSApHnKQqXXXXXXXXXX',
            'client_secret': 'wnGXZQ9X8M3TENXsMbVJ018qPPLy1EOMSs5y5AgCFXXXXXXXXXXXXXX',
            'token': response.json()['data']['access_token']
        }
        response = self.client.post(uri, data=request_data)
        assert response.status_code == 200
        assert response.json()['success'] is True
