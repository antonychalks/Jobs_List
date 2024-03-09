from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from main.models import UserProfile
from tradesman.models import Job, Task
from .forms import UpdateContactDetailsForm, UpdateUserDetailsForm, NewUserForm, NewJobForm, EditJobForm
from django.contrib.messages import get_messages

class TestPlannerViews(TestCase):

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

    def test_planner_home_view(self):
        self.client.login(username='testuser', password='password')
        response = self.client.get(reverse('planner_home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'planners/planner_home.html')

    def test_user_list_view(self):
        self.client.login(username='testuser', password='password')
        response = self.client.get(reverse('user_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'planners/list_tradesman.html')

    def test_job_edit_view(self):
        self.client.login(username='testuser', password='password')
        response = self.client.post(reverse('job_edit', args=[self.job.id, self.job.slug]), {'status': 1})
        self.assertEqual(response.status_code, 302)  # Redirects after editing
        self.assertEqual(self.job.status, 1)  # Check if job status is updated

    def test_job_delete_view(self):
        self.client.login(username='testuser', password='password')
        response = self.client.post(reverse('job_delete', args=[self.job.slug, self.job.id]))
        self.assertEqual(response.status_code, 302)  # Redirects after deletion
        self.assertFalse(Job.objects.filter(id=self.job.id).exists())  # Check if job is deleted

    def test_user_detail_view(self):
        self.client.login(username='testuser', password='password')
        response = self.client.get(reverse('user_detail', args=[self.user_profile.slug]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'planners/user_detail.html')

    def test_add_user_view(self):
        self.client.login(username='testuser', password='password')
        response = self.client.get(reverse('add_user'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'planners/add_user.html')

    def test_add_new_user(self):
        self.client.login(username='testuser', password='password')
        response = self.client.post(reverse('add_user'), {'username': 'newuser', 'password': 'password'})
        self.assertEqual(response.status_code, 200)
        self.assertTrue(User.objects.filter(username='newuser').exists())  # Check if new user is created
