from statistics import mode
from typing import TYPE_CHECKING
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class Jobs(models.Model):
    FULL_TIME = 'FT' # this will be shown in database
    PART_TIME = 'PT'
    REMOTE = 'RT'
    TIER1 = 't1'
    TIER2 = 't2'
    TIER3 = 't3'
    TIER4 = 't4'
    TIER5 = 't5'
    
    
    

    
    
    
    TYPE_CHOICES = [
        (FULL_TIME, 'Full Time'),
        (PART_TIME, 'Part Time'),
        (REMOTE, 'Remote'),
        
    ]
    
    EXP_CHOICES = [
        (TIER1, 'Less than 2yrs'),
        (TIER2, '2yrs - 5yrs'),
        (TIER3, '5yrs - 10yrs'),
        (TIER4, '10yrs - 15yrs'),
        (TIER5, 'More than 15yrs')
    ]
    
    
    title = models.CharField(max_length=200)
    company = models.CharField(max_length=100)
    location = models.CharField(max_length=200)
    salary = models.CharField(max_length=100)
    type = models.CharField(max_length=10,choices =TYPE_CHOICES, default=FULL_TIME)
    experience = models.CharField(max_length=10,choices = EXP_CHOICES, default = TIER1)
    summary = models.TextField() #text ffield is bigger than char field, more area to write stuff
    description = models.TextField() 
    requirements = models.TextField()
    logo = models.ImageField(default = 'default.png', upload_to = 'upload_imges')
    date_created = models.DateTimeField(default=timezone.now)
    owner = models.ForeignKey(User, on_delete=models.CASCADE) #odels.CASCADE means if user is deleted so will its class, also the jobs(ones created by him) will be deleted too 
    
    
    def _str_(self):
        return '{} is looking for {}'.format(self.company, self.title) #this will say "company" is looking for "title"
    

jobs=[
    {"title": "Python developer"},
    {"title": "Python developer"}
]

for job in jobs:
    print(job['title'])