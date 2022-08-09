from email.policy import default
from pickle import TRUE
from statistics import mode
from typing import TYPE_CHECKING

from unicodedata import category
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
from uuid import uuid4
from audioop import reverse

# Create your models here.
class Company(models.Model): #here we telling about the company,all its details
    title = models.CharField(max_length=200, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    uniqueId = models.CharField(null=True, blank=True, max_length=100 )
    companyLogo = models.ImageField(default = 'default.png', upload_to = 'upload_imges')
    slug = models.SlugField(max_length=500, unique=True, null=True, blank=True)
    seoDescription = models.CharField(max_length=500, null=True, blank=True)
    seoKeywords = models.CharField(max_length=500, null=True, blank=True)
    
    def __str__(self):
        return '{} - {}'.format(self.title, self.uniqueId)
    
    def get_absolute_url(self):
        return reverse('company-detail', kwargs = {'slug': self.slug }) #kwargs = {'slug': self.slug }) this will help us find company detail
    
    def save(self, *args, **kwargs):
        if self.uniqueId is None:
            self.uniqueId = str(uuid4()).split('-')[0]
            self.slug = slugify('Company {} {}'.format(self.title, self.uniqueId))
            
        self.slug = slugify('Category {} {}'.format(self.title, self.uniqueId))
        self.seoDescription = 'Apply for {} Jobs online, start your career journey today'.format(self.title)
        self.seoKeywords = '{}, Jobs,  Careers Portal, Apply Jobs'.format(self.title)
        super(Company, self).save(*args, **kwargs)

class Category(models.Model):
    title = models.CharField(max_length=200,null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    uniqueId = models.CharField(null=True, blank=True, max_length=100)
    categoryImage = models.ImageField(default = 'category.png', upload_to='upload_images')
    slug = models.SlugField(max_length=500, null=True, blank=True)
    seoDescription = models.CharField(max_length=500, null=True, blank=True)
    seoKeywords = models.CharField(max_length=500, null=True, blank=True)
    
    def _str_(self):
       return '{} - {}'.format( self.title, self.uniqueId) #this will say "company" is looking for "title"
    
    def get_absolute_url(self):
        return reverse('category-detail', kwargs={'slug': self.slug})
    
    def save(self, *args, **kwargs):
        
        if self.uniqueId is None:
            self.uniqueId = str(uuid4()).split('-')[0]
            self.slug = slugify('Category {} {}'.format(self.title, self.uniqueId))
            
        self.slug = slugify('Category {} {}'.format(self.title, self.uniqueId))
        self.seoDescription = 'Apply for {} Jobs online, start your career journey today'.format(self.title)
        self.seoKeywords = '{}, Jobs, Careers Portal, Apply Jobs'.format(self.title)
        super(Category, self).save(*args, **kwargs)
    
    

class Jobs(models.Model):
    FULL_TIME = 'FT' # this will be shown in database
    PART_TIME = 'PT'
    REMOTE = 'RT'
    TIER1 = 't1'
    TIER2 = 't2'
    TIER3 = 't3'
    TIER4 = 't4'
    TIER5 = 't5'
    NOT_PROVIDED = 'N/A'
    
    
    
    

    
    
    
    TYPE_CHOICES = [
        (FULL_TIME, 'Full Time'),
        (PART_TIME, 'Part Time'),
        (REMOTE, 'Remote'),
        (NOT_PROVIDED, 'N/A')
    ]
    
    EXP_CHOICES = [
        (TIER1, 'Less than 2yrs'),
        (TIER2, '2yrs - 5yrs'),
        (TIER3, '5yrs - 10yrs'),
        (TIER4, '10yrs - 15yrs'),
        (TIER5, 'More than 15yrs')
    ]
    
    
    title = models.CharField(max_length=200, null=True, blank=True)
    company = models.ForeignKey(Company, on_delete=models.CASCADE, null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True)
    location = models.CharField(max_length=200)
    salary = models.CharField(max_length=100)
    uniqueId = models.CharField(null=True, blank=True, max_length=100 )
    type = models.CharField(max_length=10,choices =TYPE_CHOICES, default=FULL_TIME,null=True, blank=True,)
    experience = models.CharField(max_length=10,choices = EXP_CHOICES, default = TIER1)
    summary = models.TextField(null=True, blank=True) #text ffield is bigger than char field, more area to write stuff
    description = models.TextField(null=True, blank=True) 
    requirements = models.TextField(null=True, blank=True)
    duties = models.TextField(null=True, blank=True)
    enquires = models.TextField(null=True, blank=True)
    applications =models.TextField(null=True, blank=True)
    note = models.TextField(null=True, blank=True)
    closing_date = models.DateField(null=True, blank=True)
    #logo = models.ImageField(default = 'default.png', upload_to = 'upload_imges')
    date_posted = models.DateTimeField(default=timezone.now)
    owner = models.ForeignKey(User, on_delete=models.CASCADE) #odels.CASCADE means if user is deleted so will its class, also the jobs(ones created by him) will be deleted too
    contract_type = models.CharField(max_length=100, null= True, blank=True)
    slug = models.SlugField(max_length=500, unique=True, blank=True, null=True)
    seoDescription = models.CharField(max_length=500, null=True, blank=True)
    seoKeywords = models.CharField(max_length=500, null=True, blank=True)
    urlLink = models.CharField(max_length=500, null=True, blank=True) 
    
    
    
    def _str_(self):
       return '{} - {} - {}'.format(self.company, self.title, self.location) #this will say "company" is looking for "title"
    
    def get_absolute_url(self):
        return reverse('job-detail', kwargs={'slug': self.slug})
    
    def save(self, *args, **kwargs):
        
        if self.uniqueId is None:
            self.uniqueId = str(uuid4()).split('-')[0]
            self.slug = slugify('{} {} {} {}'.format('{} {} {}'.format(self.company, self.title, self.location, self.uniqueId)))
            
        self.slug = slugify('{} {} {} {}'.format('{} {} {}'.format(self.company, self.title, self.location, self.uniqueId)))
        self.seoKeywords = 'Careers Portal, Online job application, full time jobs, part time jobs, get a job, apply for a job, {}, {}'.format(self.company.title, self.title)
        self.seoDescription = '{}'.format('Careers Portal {} Jo application. Apply for job: {} in {}, online today'.format(self.company.title, self.title, self.location))
        super(Jobs, self).save(*args, **kwargs)
    
    

jobs=[
    {"title": "Python developer"},
    {"title": "Python developer"}
]

for job in jobs:
    print(job['title'])