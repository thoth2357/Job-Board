from typing_extensions import Self
from django.db import models

# Create your models here.
class Scraping_Services(models.Model):
    url_link = models.URLField(max_length=200, null=True, blank=True)
    cron_job_time = models.TimeField(null=True, blank=True)

    def __str__(self):
        return self.url_link
    
    
