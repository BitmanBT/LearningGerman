"""This module makes settings for the admin panel"""
from django.contrib import admin
from .models import Word, Feedback


admin.site.register(Word)

@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    """To enable seeing the feedback database in the admin panel"""
    list_display = ('feedback_type', 'created_at', 'is_processed')
    list_filter = ('feedback_type', 'is_processed')
    search_fields = ('message', 'email')
