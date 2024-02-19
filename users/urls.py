from django.urls import path
from users import views as users_views


urlpatterns = [
    path('signup/', users_views.register, name='signup'), #if someone goes to /register they are gonna find it
    path('users/create/', users_views.create_resume, name='create-resume'),   # type: ignore
    path('users/view/<slug:slug>/', users_views.resume_detail, name='resume-detail'), #name shall be same as we have in reverse(), it is class based view
    path('profile/', users_views.profile, name='profile'), #if someone goes to /register they are gonna find it
    path('login/', users_views.login, name='login'),
    path('logout/', users_views.logout, name= 'logout'),   # type: ignore
    path('logging-in/', users_views.login, name= 'logging'),
]

    