from django.contrib import admin
from .models import Job, Task
from .forms import JobAdminForm


@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    """
    Lists fields for display in admin, fields for search,
    field filters, fields to prepopulate and rich-text editor.
    """
    form = JobAdminForm
    list_display = ('job_number',
                    'status',
                    'created_on',
                    'created_by',
                    'job_description',
                    'customer_name',
                    'street',
                    'postcode',
                    )
    search_fields = ['job_number', 'customer_name', 'street', 'postcode']
    list_filter = ('status', 'created_by')
    prepopulated_fields = {'slug': ('job_number',)}


admin.site.register(Task)
