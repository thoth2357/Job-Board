from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Job

from .utils import get_user_location


# Create your views here. #It tells django what html file to display
def home(request):
    user_country = get_user_location(request) #get user country based on ip-address
    print('country',user_country)
    job_list = Job.objects.all()  # import jobs from models and push it to front end
    job_list = job_list[:4]  # will display 4 jobs
    jobs_count = Job.objects.count()
    return render(request, "home.html", {"jobs": job_list, "jobs_count": jobs_count, "user_country": user_country})

def contact(request):
    '''
    purpose: View handling contact page
    args: request
    returns: Rendered contact page
    '''
    context = {}
    return render(request, "contact.html", context)

def job_list(request):
    job_list = Job.objects.all()  # import jobs from models and push it to front end
    job_list = job_list[:20]  # will display 4 jobs
    return render(request, "job-list.html", {"jobs": job_list})  # make job-list.html


def job_detail(request, slug:str):  # will take request and slug(to identify which job which it is)
    '''
    purpose: View handling job detail page
    args: request, slug
    returns: Rendered job detail page
    '''
    user_country = get_user_location(request) #get user country based on ip-address
    job = Job.objects.get(slug=slug)  # getting job with that slug
    split_title = job.title.split(' ')
    related_jobs = [Job.objects.all().filter(title__icontains = i) for i in split_title]
    non_duplicate_related_jobs = set([job for i in related_jobs for job in i])
    return render(request, "job/job_detail.html", {"job": job, "user_country":user_country, "related_jobs":non_duplicate_related_jobs, "keywords":split_title})

def job_search(request):
    return render(request, "sections/Home/job_whole_list.html", {})