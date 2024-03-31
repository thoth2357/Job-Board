from django.db import models
from django.urls import reverse
from django.template.defaultfilters import slugify
import uuid

class Contract_Type(models.Model):
    contract_type = models.CharField(max_length=50, null=True, blank=True)
    
    def __str__(self) -> str:
        return f"{self.contract_type}"
    

class Job(models.Model):
    title = models.CharField(max_length=200, null=True, blank=True)
    company = models.CharField(max_length=200, null=True, blank=True)
    category = models.CharField(max_length=200, null=True, blank=True)
    location = models.CharField(max_length=200, null=True, blank=True)
    rating = models.CharField(max_length=200, null=True, blank=True)
    salary = models.CharField(max_length=100, null=True, blank=True)
    uniqueId = models.CharField(null=True, blank=True, max_length=100)
    full_job_qualifications_duties_all = models.TextField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    requirements = models.TextField(null=True, blank=True)
    duties = models.TextField(null=True, blank=True)
    applications = models.TextField(null=True, blank=True)
    date_posted = models.DateTimeField(null=True, blank=True)
    contract_type = models.ForeignKey(Contract_Type, on_delete=models.CASCADE, null=True, blank=True)
    contract_type1 = models.CharField(max_length=200, null=True, blank=True)
    url_link = models.CharField(max_length=500, null=True, blank=True)
    source = models.CharField(max_length=100, null=True, blank=True)
    logo = models.URLField(max_length=200, null=True, blank=True)
    slug = models.SlugField(max_length=200, null=True,blank=True) #TODO Change here back to unique True, null False
    def __str__(self):
        return f"{self.title}"

    def get_absolute_url(self):
        return reverse("job_detail", kwargs={"slug": self.slug})

    def save(self, *args, **kwargs):
        if self.uniqueId is None:
            self.uniqueId = str(uuid.uuid4())
        if self.contract_type1:
            if Contract_Type.objects.filter(contract_type=self.contract_type1).exists():
                contract_model_object = Contract_Type.objects.filter(contract_type=self.contract_type1)[0]
                self.contract_type = contract_model_object
            else:
                contract_model_object = Contract_Type.objects.create(contract_type=self.contract_type1)
                self.contract_type = contract_model_object
        else:
            contract_type1 = "Onsite"
            if Contract_Type.objects.filter(contract_type=contract_type1).exists():
                contract_model_object = Contract_Type.objects.filter(contract_type=contract_type1)[0]
                self.contract_type = contract_model_object
            else:
                contract_model_object = Contract_Type.objects.create(contract_type=contract_type1)
                self.contract_type = contract_model_object
                
        if not self.slug:
            self.slug = f"{slugify(self.title)}{self.uniqueId.split('-')[1]}"
        super(Job, self).save(*args, **kwargs)

class Role(models.Model):
    role = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return f'{self.role}'
