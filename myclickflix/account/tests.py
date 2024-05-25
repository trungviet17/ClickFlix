from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import Profile
from datetime import date


class ProfileTestCase(TestCase):
    username_test = "Getup9343"
    password_test = "^V&8r6W^3G3%58$29!mu8CcNpU7&!9Rtq&!6@nbf"

    def setUp(self):
        # Create a user instance
        self.user = get_user_model().objects.create_user(
            username=self.username_test, password=self.password_test
        )

        # Create a profile instance
        self.profile = Profile.objects.create(
            user=self.user,
            date_of_birth=date(1990, 1, 1),
            address="123 Test Street",
            phone="1234567890",
            balance=100.00,
        )

    def test_profile_creation(self):
        self.assertEqual(self.profile.user.username, self.username_test)
        self.assertEqual(self.profile.date_of_birth, date(1990, 1, 1))
        self.assertEqual(self.profile.address, "123 Test Street")
        self.assertEqual(self.profile.phone, "1234567890")
        self.assertEqual(self.profile.balance, 100.00)
        self.assertEqual(str(self.profile), f"Profile of {self.user.username}")

    def test_blank_fields(self):
        # Create a new user for this test
        blank_user = get_user_model().objects.create_user(
            username="blankuser", password="password123"
        )

        # Create a profile with minimal fields for the new user
        blank_profile = Profile.objects.create(user=blank_user)

        self.assertIsNone(blank_profile.date_of_birth)
        self.assertIsNone(blank_profile.address)
        self.assertIsNone(blank_profile.phone)
        self.assertEqual(blank_profile.balance, 0)

    def test_profile_update(self):
        self.profile.date_of_birth = date(1991, 2, 2)
        self.profile.address = "456 New Address"
        self.profile.phone = "0987654321"
        self.profile.balance = 200.00
        self.profile.save()

        updated_profile = Profile.objects.get(user=self.user)
        self.assertEqual(updated_profile.date_of_birth, date(1991, 2, 2))
        self.assertEqual(updated_profile.address, "456 New Address")
        self.assertEqual(updated_profile.phone, "0987654321")
        self.assertEqual(updated_profile.balance, 200.00)

    def test_profile_deletion(self):
        user_id = self.user.id
        self.user.delete()
        with self.assertRaises(Profile.DoesNotExist):
            Profile.objects.get(user_id=user_id)
