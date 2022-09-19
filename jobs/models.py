from django.db import models
from django.urls import reverse
import uuid


class Job(models.Model):
    title = models.CharField(max_length=200, null=True, blank=True)
    company = models.CharField(max_length=200, null=True, blank=True)
    category = models.CharField(max_length=200, null=True, blank=True)
    location = models.CharField(max_length=200, null=True, blank=True)
    rating = models.CharField(max_length=200, null=True, blank=True)
    salary = models.CharField(max_length=100, null=True, blank=True)
    uniqueId = models.CharField(null=True, blank=True, max_length=100)
    description = models.TextField(null=True, blank=True)
    requirements = models.TextField(null=True, blank=True)
    duties = models.TextField(null=True, blank=True)
    applications = models.TextField(null=True, blank=True)
    date_posted = models.DateTimeField(null=True, blank=True)
    contract_type = models.CharField(max_length=100, null=True, blank=True)
    url_link = models.CharField(max_length=500, null=True, blank=True)
    source = models.CharField(max_length=100, null=True, blank=True)
    logo = models.URLField(max_length=200, null=True, blank=True)
    slug = models.SlugField(max_length=200, null=True,blank=True) #TODO Change here back to unique True, null False
    def __str__(self):
        return f"{self.company} {self.title} {self.location}"

    def get_absolute_url(self):
        return reverse("job-detail", kwargs={"slug": f"{str(uuid.uuid4()).split('-')}-{self.slug}"})

    def save(self, *args, **kwargs):
        if self.uniqueId is None:
            self.uniqueId = str(uuid.uuid4())
        if "remote" in self.location.lower():
            self.contract_type = "Remote"
        else:
            self.contract_type = "Onsite"
        super(Job, self).save(*args, **kwargs)
