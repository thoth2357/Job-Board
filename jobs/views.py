from django.shortcuts import render
from .models import Jobs


# Create your views here. #It tells django what html file to display
def home(request):
    job_list = Jobs.objects.all() #import jobs from models and push it to front end
    return render(request, 'home.html', {'jobs' : job_list}) 