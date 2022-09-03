from django.db import models

# Create your models here.
class Scraping_Service(models.Model):
    url_link = models.URLField(max_length=200, null=True, blank=True)
    is_active = models.BooleanField(default=True)
    
    def __str__(self):
        return self.url_link
    

