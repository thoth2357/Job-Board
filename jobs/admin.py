from sre_constants import CATEGORY
from django.contrib import admin
from .models import Job

# Register your models here.
admin.site.register(Job)  # creates model in the admin
# admin.site.register(Company)
# admin.site.register(Category)
