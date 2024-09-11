from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Job, Task
from .forms import UpdateJobContactDetailsForm, AddTaskForm, EditTaskForm
from multiselectfield import MultiSelectField
from main.models import UserProfile, TRADES


class TradesmanViewsTestCase(TestCase):
    def setUp(self):
        # Create a user for testing
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.client.login(username='testuser', password='testpassword')

        # Create a job for testing
        self.job = Job.objects.create(
            created_by=self.user,
            customer_name='Test Customer',
            phone='123456789',
            email='test@example.com',
            street='Test Street',
            postcode='12345',
            status=0  # Unassigned
        )

    def test_tradesman_home_view(self):
        response = self.client.get(reverse('tradesman_home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'tradesman/tradesman_home.html')

    def test_job_detail_view(self):
        response = self.client.get(reverse('job_detail', args=[self.job.slug]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'tradesman/job_detail.html')

    def test_successful_task_addition(self):
        task_data = {
            'description': 'Test Task',
            'trades_required': ['Pl'],
            'time_required': '1 hour',
            'is_completed': False,
            'add_task': '',
            'form-TOTAL_FORMS': '1',
            'form-INITIAL_FORMS': '0',
            'form-MAX_NUM_FORMS': '',
            'form-MIN_NUM_FORMS': '',
            'form-0-description': 'Test Task',
            'form-0-trades_required': 'Pl',
            'form-0-time_required': '1 hour',
            'form-0-is_completed': 'False',
        }

        response = self.client.post(reverse('job_detail', args=[self.job.slug]), data=task_data)
        self.assertEqual(response.status_code, 302)  # Redirect after successful form submission

        # Check if the task was added
        task_count = Task.objects.filter(job=self.job, description='Test Task').count()
        self.assertEqual(task_count, 1)

    def test_successful_task_edit(self):
        # Create a task for testing
        task = Task.objects.create(job=self.job, description='Original Task', time_required='2 hours')

        # Data for editing the task
        edit_task_data = {
            'description': 'Edited Task',
            'time_required': '3 hours',
        }

        response = self.client.post(reverse('task_edit', args=[task.id, self.job.slug]), data=edit_task_data)
        self.assertEqual(response.status_code, 302)  # Redirect after successful form submission

        # Check if the task was edited
        edited_task = Task.objects.get(pk=task.id)
        self.assertEqual(edited_task.description, 'Edited Task')
        self.assertEqual(edited_task.time_required, '3 hours')
