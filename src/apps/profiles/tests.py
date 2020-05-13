from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model

User = get_user_model()


class ProfileTests(TestCase):
    def test_user_create_success(self):
        data = {
            'first_name': 'Test',
            'last_name': 'User',
            'email': 'test@domain.com',
            'phone_number': '+254712345678',
            'date_of_birth': '1999-01-01'
        }
        url = reverse('profiles:profile_register')
        response = self.client.post(url, data, content_type='application/json')
        self.assertEqual(response.status_code, 200)
        queryset = User.objects.filter(username=data['email'])
        self.assertEqual(queryset.count(), 1)
        user = queryset.first()
        self.assertEqual(user.first_name, data['first_name'])
        self.assertEqual(user.last_name, data['last_name'])
        self.assertEqual(user.email, data['email'])
        self.assertIsNotNone(user.profile)
        self.assertEqual(user.profile.phone_number, data['phone_number'])
        self.assertEqual(user.profile.date_of_birth, data['date_of_birth'])
