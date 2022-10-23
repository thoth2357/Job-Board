from datetime import datetime, timedelta
import django_filters

from .models import Contract_Type, Job

from django.db.models import Q

from django import forms

from django.utils import timezone

EXPERIENCE = (
    ('No Experience', 'No Experience'),
    ('1-3 Years', '1-3 Years'),
    ('4-5 Years', '4-5 Years'),
    ('6++', 'More than 6 Years'),
)

DEGREE_CHOICES = (
    ('No Degree', 'No Degree'),
    ('High School', 'High School'),
    ('Associate', 'Associate'),
    ('Bachelor', 'Bachelor'),
    ('Master', 'Master'),
    ('Doctorate', 'Doctorate'),
    ('Professional', 'Professional'),
    ('Other', 'Other'),
    ('Not Specified', 'Not Specified'),
    ('Vocational', 'Vocational'),
    ('Certification', 'Certification'),
    ('Diploma', 'Diploma'),
    ('GED', 'GED')
)

DATE_POSTED = (
    ('Last 24 Hours', 'Last 24 Hours'),
    ('Last 3 Days', 'Last 3 Days'),
    ('Last 7 Days', 'Last 7 Days'),
    ('Last 14 Days', 'Last 14 Days'),
    ('Last 30 Days', 'Last 30 Days'),
    ('Last 60 Days', 'Last 60 Days'),
    ('Last 90 Days', 'Last 90 Days'),
)

class JobsFilter(django_filters.FilterSet):
    job_company = django_filters.CharFilter(method='custom_filter')
    location  = django_filters.CharFilter(method='custom_filter_location')
    experience_level = django_filters.ChoiceFilter(method='custom_filter_experience', empty_label="Experience Level", choices=EXPERIENCE)
    degree = django_filters.ChoiceFilter(choices=DEGREE_CHOICES, empty_label="Degree", method='custom_filter_degree')
    contract_type = django_filters.ModelChoiceFilter(queryset=Contract_Type.objects.all(), empty_label="Job Type")
    skills = django_filters.CharFilter(method='custom_filter_skills')
    date_posted = django_filters.ChoiceFilter(choices=DATE_POSTED, empty_label="Date Posted", method='custom_filter_date_posted')
    class Meta:
        model = Job
        fields = ['job_company','location', 'category', 'contract_type', 'date_posted']
        
    def custom_filter(self, queryset, title, value):
        return queryset.filter(Q(title__icontains=value) | Q(company__icontains=value) | Q(requirements__icontains=value) | Q(duties__icontains=value) | Q(description__icontains=value))
    
    def custom_filter_location(self, queryset, title, value):
        return queryset.filter(Q(location__icontains=value) | Q(location__icontains=value))
    
    def custom_filter_experience(self, queryset, title, value):
        if value == '1-3 Years':
            queryset = queryset.filter(Q(requirements__icontains="years") and Q(requirements__icontains="1") | Q(requirements__icontains="2") | Q(requirements__icontains="3"))
        elif value == '4-5 Years':
            queryset = queryset.filter(Q(requirements__icontains="years") and Q(requirements__icontains="4") | Q(requirements__icontains="5"))
        elif value == '6++':
            queryset = queryset.filter(Q(requirements__icontains="years") and Q(requirements__icontains="6") | Q(requirements__icontains="7") | Q(requirements__icontains="8") | Q(requirements__icontains="9") | Q(requirements__icontains="10") | Q(requirements__icontains="11") | Q(requirements__icontains="12") | Q(requirements__icontains="13") | Q(requirements__icontains="14") | Q(requirements__icontains="15") | Q(requirements__icontains="16") | Q(requirements__icontains="17") | Q(requirements__icontains="18") | Q(requirements__icontains="19") | Q(requirements__icontains="20") | Q(requirements__icontains="21") | Q(requirements__icontains="22") | Q(requirements__icontains="23") | Q(requirements__icontains="24") | Q(requirements__icontains="25") | Q(requirements__icontains="26") | Q(requirements__icontains="27") | Q(requirements__icontains="28") | Q(requirements__icontains="29") | Q(requirements__icontains="30") | Q(requirements__icontains="31") | Q(requirements__icontains="32") | Q(requirements__icontains="33") | Q(requirements__icontains="34") | Q(requirements__icontains="35") | Q(requirements__icontains="36") | Q(requirements__icontains="37") | Q(requirements__icontains="38") | Q(requirements__icontains="39") | Q(requirements__icontains="40") | Q(requirements__icontains="41") | Q(requirements__icontains="42") | Q(requirements__icontains="43") | Q(requirements__icontains="44") | Q(requirements__icontains="45") | Q(requirements__icontains="46") | Q(requirements__icontains="47") | Q(requirements__icontains="48") | Q(requirements__icontains="49") | Q(requirements__icontains="50") | Q(requirements__icontains="51") | Q(requirements__icontains="52") | Q(requirements__icontains="53") | Q(requirements__icontains="54") | Q(requirements__icontains="55") | Q(requirements__icontains="56") | Q(requirements__icontains="57"))
        elif value == 'No Experience':
            queryset = queryset.exclude(Q(requirements__icontains="experience"))
        return queryset
    
    def custom_filter_degree(self, queryset, title ,value):
        return queryset.filter(Q(requirements__icontains=value) | Q(requirements__icontains=value))
    
    def custom_filter_date_posted(self, queryset, title, value):
        if value == 'Last 24 Hours':
            today = datetime.now()
            day_end = today - timedelta(days=1)
            queryset = queryset.filter(date_posted__gte=day_end, date_posted__lte=today)
        elif value == 'Last 3 Days':
            today = datetime.now(tz=timezone.utc)
            day_end = today - timedelta(days=3)
            queryset = queryset.filter(date_posted__gte=day_end, date_posted__lte=today)
        elif value == 'Last 7 Days':
            today = datetime.now(tz=timezone.utc)
            day_end = today - timedelta(days=7)
            queryset = queryset.filter(date_posted__gte=day_end, date_posted__lte=today)
        elif value == 'Last 14 Days':
            today = datetime.now(tz=timezone.utc)
            day_end = today - timedelta(days=14)
            queryset = queryset.filter(date_posted__gte=day_end, date_posted__lte=today)
        elif value == 'Last 30 Days':
            today = datetime.now(tz=timezone.utc)
            day_end = today - timedelta(days=1)
            queryset = queryset.filter(date_posted__gte=day_end, date_posted__lte=today)
        elif value == 'Last 60 Days':
            today = datetime.now(tz=timezone.utc)
            day_end = today - timedelta(days=60)
            queryset = queryset.filter(date_posted__gte=day_end, date_posted__lte=today)
        elif value == 'Last 90 Days':
            today = datetime.now(tz=timezone.utc)
            day_end = today - timedelta(days=90)
            queryset = queryset.filter(date_posted__gte=day_end, date_posted__lte=today)
        return queryset