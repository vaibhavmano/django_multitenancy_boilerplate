import pytest
import unittest
from django.test import Client as TestClient
from django.contrib.auth.models import User
from rest_framework.reverse import reverse
from django.contrib.auth.models import User

from test_functions import *
from multi_tenancy.models.admin_models import Tenant


@pytest.mark.django_db
class UserTestCollectionAdmin(unittest.TestCase):

    def setUp(self):
        self.client = TestClient()
        self.tenant_obj = create_tenant()
        self.user_obj, self.tenant_user_obj = create_user(self.tenant_obj)
        session = self.client.session
        session['current_tenant_id'] = str(self.tenant_obj.id)
        session['current_user_id'] = str(self.user_obj.id)
        session['superuser'] = True
        session.save()

    @pytest.mark.skip(reason="No way of currently testing this")
    def test_create_user(self):
        uri = reverse('user_collection', args=())
        request_data = {
            'username': 'test2@prudent.ai',
            'first_name': 'test2'
        }
        response = self.client.post(uri, data=request_data)
        assert response.status_code == 201


@pytest.mark.django_db
class UserTestCollection(unittest.TestCase):

    def setUp(self):
        self.client = TestClient()
        self.tenant_obj = create_tenant()
        self.user_obj, self.tenant_user_obj = create_user(self.tenant_obj)
        session = self.client.session
        session['current_tenant_id'] = str(self.tenant_obj.id)
        session['current_user_id'] = str(self.user_obj.id)
        session['superuser'] = False
        session.save()

    def test_create_user_without_access(self):
        uri = reverse('user_collection', args=())
        request_data = {
            'username': 'test2@prudent.ai',
            'password': 'abc@12345'
        }
        response = self.client.post(uri, data=request_data)
        assert response.status_code == 422


@pytest.mark.django_db
class UserChangePasswordTest(unittest.TestCase):

    def setUp(self):
        self.client = TestClient()
        self.tenant_obj = create_tenant()
        self.user_obj, self.tenant_user_obj = create_user(self.tenant_obj)
        session = self.client.session
        session['current_tenant_id'] = str(self.tenant_obj.id)
        session['current_user_id'] = str(self.user_obj.id)
        session['superuser'] = False
        session.save()

    def test_change_password_incorrect_password(self):
        uri = reverse('change_password', args=())
        request_data = {
            'current_password': '123',
            'new_password': 'NNN@12345'
        }
        response = self.client.post(uri, data=request_data)
        assert response.status_code == 422

    def test_change_password_correct_password(self):
        uri = reverse('change_password', args=())
        request_data = {
            'current_password': 'abc@12345',
            'new_password': 'NNN@12345'
        }
        response = self.client.post(uri, data=request_data)
        assert response.status_code == 200
