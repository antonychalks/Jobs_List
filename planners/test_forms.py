from django.test import TestCase
from main.models import UserProfile
from django.contrib.auth.models import User
from .forms import UpdateContactDetailsForm, UpdateUserDetailsForm, NewUserForm, NewJobForm, EditJobForm
from tradesman.models import Job


class TestForms(TestCase):

    def setUp(self):
        self.new_user = User.objects.create(username='testUser123')

    def test_update_contact_details_form_valid(self):
        form_data = {
            'email': 'test@example.com',
            'phone': '1234567890',
            'other_phone': '0987654321',
            'street': 'Test Street',
            'town_city': 'Test City',
            'county': 'Test County',
            'postcode': '12345',
            'nok': 'Next of Kin',
            'nok_number': '9876543210',
        }
        form = UpdateContactDetailsForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_update_user_details_form_valid(self):
        form_data = {
            'profile_image': "",
            'role': 0,
            'trade': ['Pl'],
            'certifications': 'Certified',
            'medical': 'None',
        }
        form = UpdateUserDetailsForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_new_user_form_valid(self):
        UserProfile.objects.filter(user=self.new_user).delete()
        # Deletes the new_user UserProfile that was created automatically
        form_data = {
            'user': self.new_user.id,
            'role': 0,
            'profile_image': "",
            'trade': ['Pl'],
            'certifications': 'Certified',
            'medical': 'None',
            'fname': 'testFName',
            'lname': 'testLName',
            'nok': 'testNok',
            'nok_number': 'testNok_number',
            'email': 'testEmail@example.com',
            'street': 'testStreet',
            'town_city': 'testTownCity',
            'county': 'testCounty',
            'postcode': 'testPostcode',
            'phone': 'testPhone'
        }
        form = NewUserForm(data=form_data)
        print(form.errors)
        self.assertTrue(form.is_valid())

    def test_new_job_form_valid(self):
        form_data = {
            'customer_name': 'Test Customer',
            'phone': '1234567890',
            'other_phone': '0987654321',
            'email': 'test@example.com',
            'street': 'Test Street',
            'town_city': 'Test City',
            'county': 'Test County',
            'postcode': '12345',
            'job_description': 'Test Job Description',
        }
        form = NewJobForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_edit_job_form_valid(self):
        self.user = User.objects.create_user(username='testUser', password='password')
        job = Job.objects.create(created_by=self.user, customer_name='Test Customer', phone='1234567890', other_phone='0987654321',
                                 email='test@example.com', street='Test Street', town_city='Test City',
                                 county='Test County', postcode='12345', job_description='Test Job Description', status=0)
        form_data = {
            'customer_name': 'Updated Test Customer',
            'phone': '0987654321',
            'other_phone': '1234567890',
            'email': 'updated_test@example.com',
            'street': 'Updated Test Street',
            'town_city': 'Updated Test City',
            'county': 'Updated Test County',
            'postcode': '54321',
            'job_description': 'Updated Test Job Description',
            'status': 0
        }
        form = EditJobForm(data=form_data, instance=job)
        self.assertTrue(form.is_valid())
