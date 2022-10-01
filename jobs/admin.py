from django.contrib import admin
from .models import Job

@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    list_display =  ("title", "company", "location", "category", "date_posted") 
    list_filter =  ("company", "category", "date_posted") 
    search_fields = ("title", "company", "location", "category", "date_posted") 
