"""This module makes settings for the admin panel"""
from django.contrib import admin
from .models import Word


admin.site.register(Word)
