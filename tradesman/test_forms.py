from django.contrib.auth.models import User
from django.test import TestCase

from main.models import UserProfile
from .forms import JobAdminForm, UpdateJobContactDetailsForm, AddTaskForm, EditTaskForm, AssignTradesmanForm
from .models import Task, Job


class TestTradesmanForm(TestCase):
    """ Test case for testing the forms in the tradesman app."""
    def setUp(self):
        """ Sets up the test case buy creating a test user with the role of 1 (tradesman),
        creating a test job, with test tasks on the job."""
        self.user = User.objects.create_user(username='testUser9999')
        self.job = Job.objects.create(status=0, created_by=self.user)
        self.task = Task.objects.create(job=self.job, description='description')
        self.tradesmanUser = User.objects.create_user(username='tradesman')
        self.tradesmanProfile = UserProfile.objects.get(user=self.tradesmanUser)
        self.tradesmanProfile.role = 1
        self.tradesmanProfile.save()

    def test_add_task_form_valid(self):
        """ Tests the add_task_form is valid. """
        add_task_form = AddTaskForm({
            'description': 'Example description',
            'trades_required': ['El', 'Pl'],
            'time_required': '2 hours',
            'is_completed': True
        })
        self.assertTrue(add_task_form.is_valid())

    def test_add_task_form_invalid(self):
        """ Tests the add_task_form returns invalid when the trades_required field has the wrong format. """
        add_task_form = AddTaskForm({
            'description': 'Example description',
            'trades_required': ['planner'],
            'time_required': '2 hours',
            'is_completed': True
        })
        self.assertFalse(add_task_form.is_valid())

    def test_edit_task_form_valid(self):
        """ Tests the edit_task_form is valid. """
        form_data = {
            'description': 'Example description',
            'trades_required': ['El', 'Pl'],
            'time_required': '2 hours',
            'is_completed': True
        }
        form = EditTaskForm(instance=self.task, data=form_data )
        self.assertTrue(form.is_valid())
        self.assertEqual(form.cleaned_data['description'], 'Example description')

    def test_edit_task_form_invalid(self):
        """ Tests the edit_task_form returns invalid when the trades_required field has the wrong format. """
        form_data = {
            'description': 'Example description',
            'trades_required': ['planner'],
            'time_required': '2 hours',
            'is_completed': True
        }
        form = EditTaskForm(instance=self.task, data=form_data )
        self.assertFalse(form.is_valid())

    def test_assign_tradesman_form_valid(self):
        """ Tests the assign_tradesman_form is valid. """
        form_data = {
            'tradesman_assigned': [self.tradesmanProfile.id,]
        }
        form = AssignTradesmanForm(instance=self.task, data=form_data)
        if form.is_valid():
            form.save()
        self.assertTrue(form.is_valid())
        self.assertIn(self.tradesmanProfile, self.task.tradesman_assigned.all())

    def test_assign_tradesman_form_invalid(self):
        """ Tests the assing_tradesman_form returns invalid when the tradesman_assigned field is passed a string
        rather than an object. """
        form_data = {
            'tradesman_assigned': 'example tradesman name'
        }
        form = AssignTradesmanForm(instance=self.task, data=form_data)
        if form.is_valid():
            form.save()
        self.assertFalse(form.is_valid())

    def test_update_contact_details_form_valid(self):
        """ Tests the update_contact_details_form is valid. """
        form_data = {
            'customer_name': 'John Doe',
            'phone': '0712547854',
            'other_phone': '07565487854',
            'email': 'john@doe.com',
            'street': 'street',
            'town_city': 'town',
            'county': 'county',
            'postcode': 'EX4MPL'
        }
        form = UpdateJobContactDetailsForm(instance=self.job, data=form_data)
        self.assertTrue(form.is_valid())
        self.assertIn('John Doe', self.job.customer_name)

    def test_update_contact_details_form_invalid(self):
        """ Tests the update_contact_details_form returns invalid when the form is invalid. """
        form_data = {
            'customer_name': 'John Doe',
            'phone': '0712547854',
            'other_phone': '07565487854',
            'email': 'john@doe.com',
            'street': 'street',
            'town_city': 'town',
            'county': 'county',
            'postcode': 'EX4MPLfesfsfs'
        }
        form = UpdateJobContactDetailsForm(instance=self.job, data=form_data)
        self.assertFalse(form.is_valid())
