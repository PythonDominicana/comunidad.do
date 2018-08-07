import unittest
import random
import string
import pytest
from django.urls import reverse, reverse_lazy
from django.test import Client
from django.contrib.contenttypes.models import ContentType
from comunidaddo.users.models import User
from comunidaddo.events.models import Event, Region


pytestmark = pytest.mark.django_db

def random_string(length):
    strings = random.choice(string.ascii_uppercase + string.digits)
    return ''.join(strings for _ in range(length))


def create_django_contrib_auth_models_user(**kwargs):
    defaults = {}
    defaults["username"] = random_string(15)
    defaults["email"] = "username@tempurl.com"
    defaults.update(**kwargs)
    return User.objects.create(**defaults)


def create_django_contrib_auth_models_group(**kwargs):
    defaults = {}
    defaults["name"] = "group"
    defaults.update(**kwargs)
    return Group.objects.create(**defaults)


def create_django_contrib_contenttypes_models_contenttype(**kwargs):
    defaults = {}
    defaults.update(**kwargs)
    return ContentType.objects.create(**defaults)


def create_event(**kwargs):
    defaults = {}
    defaults["title"] = "title"
    defaults["description"] = "description"
    defaults["url"] = "url"
    defaults["image"] = "image"
    defaults["start_date"] = "2018-07-22"
    defaults["end_date"] = "2018-07-22"
    defaults["address"] = "address"
    defaults["country"] = "country"
    defaults["city"] = "city"
    defaults.update(**kwargs)
    if "user" not in defaults:
        defaults["user"] = create_django_contrib_auth_models_user()
    if "region" not in defaults:
        defaults["region"] = create_region()
    return Event.objects.create(**defaults)


def create_region(**kwargs):
    defaults = {}
    defaults["name"] = "name"
    defaults.update(**kwargs)
    return Region.objects.create(**defaults)



class EventViewTest(unittest.TestCase):
    '''
    Tests for Event
    '''
    def setUp(self):
        self.client = Client()

    def test_list_event(self):
        url = '/events/'
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_event(self):
        url = '/events/create/'
        data = {
            "title": "title",
            "description": "description",
            "start_date": "2018-07-18",
            "end_date": "2018-07-18",
            "address": "address",
            "country": "country",
            "city": "city",
            "user": create_django_contrib_auth_models_user().pk,
            "region": create_region().pk,
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_event(self):
        event = create_event()
        url = f"/events/{event.slug}/"
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_event(self):
        event = create_event()
        data = {
            "title": "title",
            "description": "description",
            "start_date": "2018-07-18",
            "end_date": "2018-07-18",
            "address": "address",
            "country": "country",
            "city": "city",
            "user": create_django_contrib_auth_models_user().pk,
            "region": create_region().pk,
        }
        url = f"/events/update/{event.slug}/"
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)
