from pickle import FALSE
from urllib.request import Request
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import * # * means all forms will get imported same for models below
from .models import *
from django.contrib.auth.decorators import login_required
from django.views.generic import DetailView
from datetime import datetime



# Create your views here.
def login(request):
    pass

def register(request):
    if request.method == 'GET': #when you request a form it is in a get request 
        form = RegisterForm()
        context = {'form' : form} #this creates a object which you want to send to the front end
        return render(request, 'signup-login.html', context) # here we pushing that form to the html page 
    
    if request.method == 'POST': #when you submit a form it is POST request
        form = RegisterForm(request.POST)
        if form.is_valid():
             form.save()
             user = form.cleaned_data.get('username')
             messages.success(request, 'Account was created for' + user)
             return redirect('home_page')
        else:
            messages.error(request, 'Error Processing Your Request')
            context = {'form' : form}
            return render(request, 'signup-login.html', context)

    return render(request, 'signup-login.html', {})

@login_required #This makes sure that only people who have logged in can access the profile page
def profile(request):
    return render(request, 'profile.html' , {})

#@login_required 
def create_resume(request):
    if request.method == 'POST':
        form = ResumeForm(request.POST, request.Files) #so you will say that its the resume form but it has request.POST or request.Files, different than registerform because resume form has some file data
        if form.is_valid(): # important to this so that all form validations happen
            obj = forms.save(commit = FALSE)
            
            obj.user = request.user #this wont be null as we getting user when we logged in
            
            obj.save()
            
            messages.success(request, 'Resume Created Successfully')
            return redirect('profile')
        else:
            messages.error(request, 'Error Processing your Request')
            context = {'form' : form }
            return render(request, 'create-resume.html', context)
    if request.method == 'GET':
        form = ResumeForm()
        context = {'form': form}
        return render(request, 'create-resume.html', context) # passing in context means you are passing  context = {'form': form}


class ResumeDetailView(DetailView):
    model = Resume
    template_name = 'resume-detail.html'