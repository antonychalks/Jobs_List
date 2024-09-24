from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from main.models import UserProfile


class TestMainViews(TestCase):

    def setUp(self):
        """ Sets up a test user, with profile and test data inputted."""
        self.user = User.objects.create_user(username='testUser', password='password')
        self.profile = UserProfile.objects.get(
            user=self.user,
        )
        self.profile.role = 0
        self.profile.slug = 'testUser'
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

    def test_landing_page_view_authenticated_user(self):
        """ Test the landing page loads correctly if a user is authenticated."""
        self.client.login(username='testUser', password='password')
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'main/index.html')
        self.assertEqual(response.context['user_profile'], self.profile)

    def test_landing_page_view_unauthenticated_user(self):
        """ Test the landing page loads correctly if a user is not authenticated."""
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'main/index.html')
        self.assertIsNone(response.context['user_profile'])

    def test_landing_page_view_initial_signup(self):
        """Tests the user gets redirected to the initial sign-up page if they have not completed the initial sign-up."""
        self.client.login(username='testUser', password='password')
        self.profile.is_initial_signup = True
        self.profile.save()
        response = self.client.get(reverse('home'))
        self.assertRedirects(response, reverse('user_profile_signup'), status_code=302, target_status_code=200)

    def test_user_profile_signup_view(self):
        """ Tests the initial signup page."""
        self.client.login(username='testUser', password='password')
        self.profile.is_initial_signup = True
        self.profile.save()
        response = self.client.get(reverse('user_profile_signup'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'main/user_profile_signup.html')
        self.assertEqual(response.context['user'], self.user)

    def test_user_profile_signup_view_submit_form(self):
        """ Tests the initial signup page form is submitted correctly."""
        self.client.login(username='testUser', password='password')
        user_profile = UserProfile.objects.get(user=self.user)
        response = self.client.post(reverse('user_profile_signup'), data={
            'fname': 'testFName',
            'lname': 'testLName',
            'email': 'testEmail',
            'phone': 'testPhone',
            'role': 0,
            'trade': 'pl',
        })

        self.assertEqual(response.status_code, 200)
        self.assertEqual(user_profile.fname, 'testFName')
