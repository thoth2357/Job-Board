from enum import unique
from django.db import models

# Create your models here.
class Scraping_Service(models.Model):
    url_link = models.URLField(max_length=200, null=True, blank=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.url_link

class Filter_tag(models.Model):
    '''
    model to use for filter tagging
    '''
    
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
    tag_name = models.CharField(max_length=25, null=True, blank=True, unique=True, help_text="Tag name to use for filtering. Must be unique.")
    tag_description = models.TextField(max_length=100, null=True, blank=True)
    tag_search_company = models.CharField(max_length=100, null=True, blank=True,default='', help_text="Companies name to search for")
    tag_search_category = models.CharField(max_length=100, null=True, blank=True,default='',  help_text="Categories to search for")
    tag_search_location = models.CharField(max_length=100, null=True, blank=True,default='',  help_text="Locations to search for")
    search_url = models.URLField(max_length=200, null=True, blank=True, help_text="Automatically generated..Readonly Field can't be edited")
    tag_experience_level = models.CharField(max_length=25, null=True, blank=True, choices=EXPERIENCE, help_text="Experience level to search for")
    tag_contract_type = models.ForeignKey("jobs.Contract_Type",on_delete=models.CASCADE, null=True, blank=True, help_text="Contract type to search for")
    tag_degree = models.CharField(max_length=25, null=True, blank=True, choices=DEGREE_CHOICES, help_text="Degree to search for")
    tag_date_posted = models.CharField(max_length=25, null=True, blank=True, choices=DATE_POSTED, help_text="Date posted to search for")
    tag_role = models.ForeignKey("jobs.Role",on_delete=models.CASCADE, null=True, blank=True, help_text="Role to search for")
    
    def __str__(self) -> str:
        return f"{self.tag_name}"
    
    def save(self, *args, **kwargs):
        if not self.tag_search_company:
            self.tag_search_company = ' '
        if not self.tag_search_category:
            self.tag_search_category = ' '
        if not self.tag_search_location:
            self.tag_search_location = ' '

        if self.tag_search_company is not None and self.tag_search_category is not None and self.tag_search_location is not None:
            self.search_url = f"?q=job_company={self.tag_search_company.replace(',','')}&location={self.tag_search_location}&category={self.tag_search_category}"
        super(Filter_tag, self).save(*args, **kwargs)