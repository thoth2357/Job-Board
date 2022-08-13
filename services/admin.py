from django.contrib import admin
from .models import Scraping_Service

# Register your models here.
# admin.site.register(Scraping_Services) # creates model in the admin


@admin.register(Scraping_Service)
class Scraping_ServiceAdmin(admin.ModelAdmin):
    list_display = ('url_link', 'is_active')
    list_filter = ('is_active',)
    search_fields = ('url_link',)
    ordering = ('url_link',)
    actions = ['make_active', 'make_inactive']

    def make_active(self, request, queryset):
        queryset.update(is_active=True)

    def make_inactive(self, request, queryset):
        queryset.update(is_active=False)
    make_active.short_description = "Mark selected services as active"
    make_inactive.short_description = "Mark selected services as inactive"
    actions = [make_active, make_inactive]