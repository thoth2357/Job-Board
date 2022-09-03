from sre_constants import CATEGORY
from django.contrib import admin
from .models import Jobs

# Register your models here.
admin.site.register(Jobs) # creates model in the admin
# admin.site.register(Company)
# admin.site.register(Category)
