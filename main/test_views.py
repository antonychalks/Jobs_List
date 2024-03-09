from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from main.models import UserProfile
from tradesman.models import Job, Task

class TestMainViews(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='password')
        self.user_profile = UserProfile.objects.create(
            user=self.user,
            role=0,
            slug='testuser'
        )

        self.job = Job.objects.create(
            created_by=self.user,
            customer_name="Test Customer",
            status=0,
            slug='test-job'
        )

        self.task = Task.objects.create(
            job=self.job,
            description="Test Task",
            is_completed=False
        )

    def test_landing_page_view_authenticated_user(self):
        self.client.login(username='testuser', password='password')
        response = self.client.get(reverse('landing_page'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'main/index.html')
        self.assertEqual(response.context['user_profile'], self.user_profile)
        self.assertEqual(response.context['job'], Job)
        self.assertEqual(response.context['task'], Task)

    def test_landing_page_view_unauthenticated_user(self):
        response = self.client.get(reverse('landing_page'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'main/index.html')
        self.assertIsNone(response.context['user_profile'])
        self.assertEqual(response.context['job'], Job)
        self.assertEqual(response.context['task'], Task)
