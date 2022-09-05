from django.shortcuts import render
from .models import Job


# Create your views here. #It tells django what html file to display
def home(request):
    job_list = Jobs.objects.all() #import jobs from models and push it to front end
    job_list = job_list[:4] #will display 4 jobs
    return render(request, 'home.html', {'jobs' : job_list}) 

def job_list(request):
    job_list = Jobs.objects.all() #import jobs from models and push it to front end
    job_list = job_list[:20] #will display 4 jobs
    return render(request, 'job-list.html', {'jobs' : job_list}) #make job-list.html

def job_detail(request, slug): #will take request and slug(to identify which job which it is)
   the_job = Jobs.objects.get(slug = slug) #getting job with that slug
   return render(request, 'job-detail.html',{'object': the_job}) 
    