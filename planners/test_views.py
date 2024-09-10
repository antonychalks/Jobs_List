from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from main.models import UserProfile
from tradesman.models import Job, Task
from .forms import UpdateContactDetailsForm, UpdateUserDetailsForm, NewUserForm, NewJobForm, EditJobForm
from django.contrib.messages import get_messages


class TestPlannerViews(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='testUser', password='password')
        self.profile = UserProfile.objects.get(
            user=self.user,
        )
        self.profile.role = 0
        self.profile.fname = 'testFName'
        self.profile.lname = 'testLName'
        self.profile.medical = 'testMedical'
        self.profile.nok = 'testNok'
        self.profile.nok_number = 'testNok_number'
        self.profile.certifications = 'testCertifications'
        self.profile.email = 'testEmail'
        self.profile.street = 'testStreet'
        self.profile.town_city = 'testTownCity'
        self.profile.county = 'testCounty'
        self.profile.postcode = 'testPostcode'
        self.profile.phone = 'testPhone'
        self.profile.profile_complete = True
        self.profile.is_initial_signup = False
        self.profile.save()

        self.job = Job.objects.create(
            created_by=self.user,
            customer_name="Test Customer",
            email="testemail@test.com",
            phone="07123456789",
            street="testStreet",
            postcode="testPostcode",
            job_description="testDescription",
            slug='test-job',
            status=0
        )
        self.job.status = Job.set_job_status(self.job)


    def test_planner_home_view(self):
        self.client.login(username='testUser', password='password')
        response = self.client.get(reverse('planner_home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'planners/planner_home.html')

    def test_user_list_view(self):
        self.client.login(username='testUser', password='password')
        response = self.client.get(reverse('UserList'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'planners/list_user.html')

    def test_job_edit_view(self):
        self.client.login(username='testUser', password='password')
        response = self.client.post(reverse('job_edit', args=[self.job.slug, self.job.id]), {'email': 'test@test.com'})
        self.assertEqual(response.status_code, 302)
        self.assertEqual(self.job.email, 'test@test.com')

    def test_job_delete_view(self):
        self.client.login(username='testUser', password='password')
        response = self.client.post(reverse('job_delete', args=[self.job.slug, self.job.id]))
        self.assertEqual(response.status_code, 302)
        self.assertFalse(Job.objects.filter(id=self.job.id).exists())

    def test_user_detail_view(self):
        self.client.login(username='testUser', password='password')
        self.profile.slug = "exampleSlug"
        self.profile.save()
        response = self.client.get(reverse('user_detail', args=[self.profile.slug]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'planners/user_detail.html')

    def test_add_user_view(self):
        self.client.login(username='testUser', password='password')
        response = self.client.get(reverse('add_user'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'planners/add_user.html')

    def test_add_new_user(self):
        self.user = User.objects.create_user(username='newUser', password='password')
        self.client.login(username='testUser', password='password')
        response = self.client.post(reverse('add_user'), data={
            'User': 'newUser',
            'fname': 'testFName',
            'lname': 'testLName',
            'email': 'testEmail',
            'phone': 'testPhone',
            'role': 0,
            'trade': 'pl',
        })
        self.assertEqual(response.status_code, 200)
        self.assertTrue(User.objects.filter(username='newUser').exists())  # Check if new user is created
