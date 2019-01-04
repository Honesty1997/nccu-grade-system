from django.test import TestCase
from django.db import IntegrityError, transaction
from .models import User

# Create your tests here.
class UserTestCase(TestCase):
    def setUp(self):
        User.objects.create_user
    
    def test_can_create_user(self):
        User.objects.create_user('apple', 'somepassword')
        User.objects.create_user('someapple', 'somepassword')
        user_1, user1_is_new = User.objects.get_or_create(account='apple')
        user_2, user2_is_new = User.objects.get_or_create(account='someapple')
        self.assertFalse(user1_is_new)
        self.assertFalse(user2_is_new)
        self.assertIsNotNone(user_1)
        self.assertIsNotNone(user_2)

    def test_can_create_superuser(self):
        User.objects.create_superuser('superbigapple', 'somepassword')
        User.objects.create_superuser('supersomeapple', 'somepassword')
        user_1, user1_is_new = User.objects.get_or_create(
            account='superbigapple')
        user_2, user2_is_new = User.objects.get_or_create(
            account='supersomeapple')
        self.assertFalse(user1_is_new)
        self.assertFalse(user2_is_new)
        self.assertIsNotNone(user_1)
        self.assertIsNotNone(user_2)
        self.assertTrue(user_1.is_admin)
        self.assertTrue(user_2.is_admin)
    
    def test_throwing_error_duplicate_account(self):
        User.objects.create_user('test', 'testpassword')
        User.objects.create_superuser('ttt', 'tttttttt')
        with transaction.atomic():
            with self.assertRaises(IntegrityError):
                User.objects.create_user('test', 'testpassword')
        with transaction.atomic():
            with self.assertRaises(IntegrityError):
                User.objects.create_superuser('ttt', 'tttttttt')
    
    def test_user_login(self):
        User.objects.create_user('testisboring', 'reallyboring')
        test_user = User.objects.get(account='testisboring')
