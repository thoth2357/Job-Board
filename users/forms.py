from email.mime import image
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .forms import *
from .models import *
#from django.contrib.auth.decorators import login

from .models import Resume

class DateInput(forms.DateInput): #whhat this does is allow us to ask date in a date format rather than in a text format so later on when we use it with forms.dateinput it shall show a date entering field or else it would have shown a textfield
    input_type: 'date'

class RegisterForm(UserCreationForm):
    email = forms.EmailField(max_length=100,help_text='Enter Email Address', required=True,widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Email'}))
    
    first_name = forms.CharField(max_length=100,help_text='Enter First Name', required=True,widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'}))
    
    last_name = forms.CharField(max_length=100,help_text='Enter Last Name', required=True,widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name'}))
    
    username = forms.CharField(max_length=100,help_text='Enter Username', required=True,widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}))
    
    password1 = forms.CharField(max_length=200,help_text='Enter Password', required=True,widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}))
    
    password2 = forms.CharField(max_length=200,help_text='Enter your Password again', required=True,widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}))  
    
    #check = forms.BooleanField(required = True)
    
    class Meta:
        model = User
        fields = [
            'username', 'email', 'first_name', 'last_name', 'password1', 'password2' #, 'check'
        ]
        
class ResumeForm(forms.ModelForm):
    
    BLACK = 'Black'
    WHITE = 'White'
    COLOURED = 'Coloured'
    INDIAN = 'Indian'
    CHINESE = 'Chinese'
    
    MALE = 'Male'
    FEMALE = 'Female'
    OTHER = 'Other'
    MARRIED = 'Married'
    SINGLE = 'Single'
    WIDOWED = 'Widowed'
    DIVORCED = 'Divorced'
    
    GAUTENG = 'Gauteng'
    MPUMALANGA = 'Mpumalanga'
    FREE_STATE = 'Free-state'
    NORTH_WEST = 'North-west'
    LIMPOPO = 'Limpopo' 
    WESTER_CAPE = 'Western-cape'
    NOTHERN_CAPE = 'Nothern-cape'
    EASTERN_CAPE = 'Eastern-cape'
    KWAZULU_NATAL = 'Kwazulu-natal'
    
    ETHINIC_CHOICES = [
        (BLACK, 'Black'),
        (WHITE, 'White'),
        (COLOURED, 'Coloured'),
        (INDIAN, 'Indian'),
        (CHINESE, 'Chinese'),
    ]
    
    SEX_CHOICES = [
        (MALE, 'Male'),
        (FEMALE, 'Female'),
        (OTHER, 'Other'),
    ]
    
    MARITAL_STATUS =[
        (MARRIED,'Married'),
        (SINGLE,'Single'),
        (WIDOWED, 'Widowed'),
        (DIVORCED, 'Divorced')
    ]
    
    PROVINCE_CHOICES = [
        (GAUTENG, 'Gauteng'),
        (MPUMALANGA, 'Mpumalanga'),
        (FREE_STATE, 'Free-state'),
        (NORTH_WEST, 'North-west'),
        (LIMPOPO, 'Limpopo' ),
        (WESTER_CAPE, 'Western-cape'),
        (NOTHERN_CAPE, 'Nothern-cape'),
        (EASTERN_CAPE, 'Eastern-cape'),
        (KWAZULU_NATAL, 'Kwazulu-natal')
        
    ]
    
    IMAGES = [
        'person1.jpg', 'person2.jpg', 'person3.jpg', 
        'person4.jpg', 'person5.jpg', 'person6.jpg', 
    ]
    
    image = forms.ImageField(required=False, widget=forms.FileInput(attrs={'class': 'form-control'})) # you specifically have to say required = false, if it is not required. Will get an error otherwise. 'class': 'form-control', this is the class we getting from the HTML class
    ethnicity = forms.ChoiceField(choices = ETHINIC_CHOICES, widget=forms.Select(attrs={'class': 'nice-select rounded'}))
    date_birth = forms.DateField(required=True, widget=forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'Enter a date: '})) #recheck this
    sex =  forms.ChoiceField(choices = SEX_CHOICES, widget=forms.Select(attrs={'class': 'nice-select rounded'}))
    marital_status = forms.ChoiceField(choices = MARITAL_STATUS, widget=forms.Select(attrs={'class': 'nice-select rounded'}))
    addressLine1 = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control resume', 'placeholder': 'Enter Address Line 1'}))
    addressLine2 = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control resume', 'placeholder': 'Enter Address Line 2'}))
    suburb = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control resume', 'placeholder': 'Enter Suburb'}))
    city = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control resume', 'placeholder': 'Enter City'}))
    province = forms.ChoiceField(choices = PROVINCE_CHOICES, widget=forms.Select(attrs={'class': 'nice-select rounded'}))
    phoneNumber = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control resume', 'placeholder': 'Enter Phone Number'}))
    cover_letter = forms.FileField(required=False, widget=forms.FileInput(attrs={'class': 'form-control'}))
    cv = forms.FileField(required=False, widget=forms.FileInput(attrs={'class': 'form-control'}))
    
    class Meta:
        model = Resume
        fields = [
            'image',
            'ethnicity',
         'date_birth',  
            'sex', 
        'marital_status', 
         'addressLine1',
          'addressLine2', 
        'suburb', 
         'city',
        'province',
        'phoneNumber',
        'cover_letter',
         'cv'
        ]