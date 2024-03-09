from django.test import TestCase
from .forms import JobAdminForm, UpdateJobContactDetailsForm, AddTaskForm, EditTaskForm

class TestAddTaskForm(TestCase):
    # Test AddTaskForm
    def test_add_task_form_valid(self):
        add_task_form = AddTaskForm({
            'description': 'Example description',
            'trades_required': ['El', 'Pl'],
            'time_required': '2 hours',
            'is_completed': True
        })
        self.assertTrue(add_task_form.is_valid())
