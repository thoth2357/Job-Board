"""jobWebsite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from re import template
from django.contrib import admin
from django.urls import path
from jobs import views as jobs_views      #from the job application it is gonna import views
from users import views as users_views
from django.contrib.auth import views as auth_views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', jobs_views.home, name='home_page'),   #this is home function inside the views.py in the jobs folder
    path('register/', users_views.register, name='signup-login_page'), #if someone goes to /register they are gonna find it
    path('users/create/', users_views.create_resume, name='create-resume'), #
    path('users/view/<slug:slug>/', users_views.ResumeDetailView.as_view(), name='create-resume'), #
    path('profile/', users_views.profile, name='profile'), #if someone goes to /register they are gonna find it
    path('login/', auth_views.LoginView.as_view(template_name = 'login.html'), name= 'login'), #this will be class based view.For class based view, have to add as_view in the end
    path('logout/', auth_views.LogoutView.as_view(template_name = 'logout.html'), name= 'logout'), 
    path('logging-in/', users_views.login, name= 'logging'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT) #this will get images to appear, this step is necessary with adding MEDIA ROOT to the settings.py file. We are doing these to make sure all the images the user uploads are getting displayed on the website
