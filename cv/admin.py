from django.contrib import admin
from .models import CV

@admin.register(CV)
class CVAdmin(admin.ModelAdmin):
    list_display = ('profession', 'full_name', 'schedule', 'employment', 
            'education', 'salary', 'experience', 'skills', 
            'achievements', 'expectations', 'add_info', 'feedback')
    # list_display_links = ('id', 'title')
    # search_fields = ('profession', 'full_name', 'salary')
    # list_editable = ('feedback',)
    # list_filter = ('feedback',)
