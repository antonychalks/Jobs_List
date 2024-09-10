from django.test import TestCase
from main.models import UserProfile
from django.contrib.auth.models import User
from .forms import InitialSignUpForm
from tradesman.models import Job


class TestForms(TestCase):

    def test_initial_signUp_form_valid(self):
        form_data = {
            'fname': 'testFName',
            'lname': 'testLName',
            'phone': '1234567890',
            'email': 'test@test.com',
            'role': '0',
            'trade': ['AD'],
        }
        form = InitialSignUpForm(data=form_data)
        if form.is_valid():
            self.assertTrue(form.is_valid())
        else:
            print(form.errors)
            self.assertTrue(form.is_valid())

    def test_initial_signUp_form_invalid_fname_lname(self):
        form_data = {
            'fname': '',
            'lname': '',
            'phone': '1234567890',
            'email': 'test@test.com',
            'role': 0,
            'trade': ['AD'],
        }
        form = InitialSignUpForm(data=form_data)
        self.assertFalse(form.is_valid())

    def test_initial_signUp_form_invalid_phone(self):
        form_data = {
            'fname': 'testFName',
            'lname': 'testLName',
            'phone': '',
            'email': 'test@test.com',
            'role': 0,
            'trade': ['AD'],
        }
        form = InitialSignUpForm(data=form_data)
        self.assertFalse(form.is_valid())

    def test_initial_signUp_form_invalid_email(self):
        form_data = {
            'fname': 'testFName',
            'lname': 'testLName',
            'phone': '1234567890',
            'email': 'test',
            'role': 0,
            'trade': ['AD'],
        }
        form = InitialSignUpForm(data=form_data)
        self.assertFalse(form.is_valid())

    def test_initial_signUp_form_invalid_role(self):
        form_data = {
            'fname': 'testFName',
            'lname': 'testLName',
            'phone': '1234567890',
            'email': 'test',
            'role': '',
            'trade': ['AD'],
        }
        form = InitialSignUpForm(data=form_data)
        self.assertFalse(form.is_valid())

    def test_initial_signUp_form_invalid_trade(self):
        form_data = {
            'fname': 'testFName',
            'lname': 'testLName',
            'phone': '1234567890',
            'email': 'test',
            'role': 0,
            'trade': 'AD',
        }
        form = InitialSignUpForm(data=form_data)
        self.assertFalse(form.is_valid())