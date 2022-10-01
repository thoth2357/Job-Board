from django.contrib import admin
from .models import Scraping_Service, Filter_tag

# Register your models here.
# admin.site.register(Scraping_Services) # creates model in the admin


@admin.register(Scraping_Service)
class Scraping_ServiceAdmin(admin.ModelAdmin):
    list_display = ("url_link", "is_active")
    list_filter = ("is_active",)
    search_fields = ("url_link",)
    ordering = ("url_link",)

    def make_active(self, request, queryset):
        queryset.update(is_active=True)

    def make_inactive(self, request, queryset):
        queryset.update(is_active=False)

    make_active.short_description = "Mark selected services as active"
    make_inactive.short_description = "Mark selected services as inactive"
    actions = [make_active, make_inactive]

@admin.register(Filter_tag)
class FilterTagAdmin(admin.ModelAdmin):
    list_display = ("tag_name", "tag_description", "tag_search_company", "tag_search_category")
    list_filter = ("tag_name",)
    search_fields = ("tag_name", "tag_description", "tag_search_company", "tag_search_category")
    ordering = ("tag_name",)
    
    readonly_fields = ['search_url']
    

    def render_change_form(self, request, context, *args, **kwargs):
        form_instance = context['adminform'].form
        form_instance.fields['tag_name'].widget.attrs['placeholder'] = 'E.g. GMStrat'
        form_instance.fields['tag_description'].widget.attrs['placeholder'] = 'E.g. Tag For Finding Strategy Jobs in Google and Microsoft'
        form_instance.fields['tag_search_company'].widget.attrs['placeholder'] = 'E.g. google, Microsoft'
        form_instance.fields['tag_search_category'].widget.attrs['placeholder'] = 'E.g. Strategy'
        # form_instance.fields['search_url'].widget.attrs['placeholder'] = 'Please Leave Blank. It is auto generated.'
        return super().render_change_form(request, context, *args, **kwargs)