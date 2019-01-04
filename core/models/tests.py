from django.test import TestCase
from django.db import IntegrityError, transaction
from .models import Person

class PersonTestCase(TestCase):
    def setUp(self):
        pass

    def test_can_create_person(self):
        self.assertFalse(True)
