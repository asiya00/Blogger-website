from django.test import TestCase
from django.contrib.auth.models import User
# Create your tests here.

class Profile(TestCase):

    def test_user_model_has_profile(self):
        user = User(
        email="user@gmail.com",
        username="user",
        password="abcxyz123"
        )
        user.save()

        self.assertTrue(hasattr(user, 'profile'))
