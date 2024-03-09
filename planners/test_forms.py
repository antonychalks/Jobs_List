from django.test import TestCase
from main.models import UserProfile
from django.contrib.auth.models import User
from main.forms import UpdateContactDetailsForm, UpdateUserDetailsForm, NewUserForm, NewJobForm, EditJobForm
from tradesman.models import Job

class TestForms(TestCase):

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
            'profile_image': 'test.jpg',
            'role': 0,
            'trade': ['Plumber'],
            'certifications': 'Certified',
            'medical': 'None',
        }
        form = UpdateUserDetailsForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_new_user_form_valid(self):
        form_data = {
            'user': User.objects.create(username='testuser'),
            'role': 0,
            'trade': ['Plumber'],
            'certifications': 'Certified',
            'medical': 'None',
        }
        form = NewUserForm(data=form_data)
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
        job = Job.objects.create(customer_name='Test Customer', phone='1234567890', other_phone='0987654321',
                                 email='test@example.com', street='Test Street', town_city='Test City',
                                 county='Test County', postcode='12345', job_description='Test Job Description')
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
        }
        form = EditJobForm(data=form_data, instance=job)
        self.assertTrue(form.is_valid())
