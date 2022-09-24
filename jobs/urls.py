from django.urls import path,include
from jobs import views as jobs_views  #from the job application it is gonna import views

urlpatterns = [
    path('', jobs_views.home, name='home'),   #this is home function inside the views.py in the jobs folder
    path('contact',jobs_views.contact, name='contact'),
    path('jobs/', jobs_views.job_list, name='job-list'),
    path('jobs/<slug:slug>', jobs_views.job_detail, name='job-detail'), #slug will help us identify the specific instance of job
]

