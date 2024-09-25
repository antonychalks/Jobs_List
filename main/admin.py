from django.contrib import admin
from .models import UserProfile
from django_summernote.admin import SummernoteModelAdmin


# Register your models here.
@admin.register(UserProfile)
class PostAdmin(SummernoteModelAdmin):
    """
    Lists fields for display in admin, fields for search,
    field filters, fields to prepopulate and rich-text editor.
    """

    list_display = ('user', 'role', 'get_trade_display',
                    'fname', 'lname', 'slug')
    search_fields = ['user', 'fname', 'lname']
    list_filter = ('role', 'trade', )
    prepopulated_fields = {'slug': ('fname', 'lname',)}
    summernote_fields = ('content',)
