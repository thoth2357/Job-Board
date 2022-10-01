import django_filters

from .models import Job

from django.db.models import Q

from django import forms


class JobsFilter(django_filters.FilterSet):
    job_company = django_filters.CharFilter(method='custom_filter')
    # contract_type = django_filters.BooleanFilter(widget=forms.CheckboxInput)
    class Meta:
        model = Job
        fields = ['job_company','location', 'category']
        
    def custom_filter(self, queryset, title, value):
        return queryset.filter(Q(title__icontains=value) | Q(company__icontains=value))