from django.test import TestCase
from .forms import InitialSignUpForm


class TestForms(TestCase):

    def test_initial_signUp_form_valid(self):
        """ Tests the initial sign up form returns as valid when the form is valid. """
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
        """ Tests the initial sign up form returns as invalid when the form is invalid
        due to missing first and last names"""
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
        """ Tests the initial sign up form returns as invalid when the form is invalid due to missing phone number."""
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
        """ Tests the initial sign up form returns as invalid when the form is invalid due to invalid email format."""
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
        """ Tests the initial sign up form returns as invalid when the form is invalid due to invalid role."""
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
        """ Tests the initial sign up form returns as invalid when the form is invalid due to invalid trade input."""
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
