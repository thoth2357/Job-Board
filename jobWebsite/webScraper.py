
from cgi import test
import email
from turtle import title
import requests
from bs4 import BeautifulSoup
import json

import pandas as pd
from datetime import date

from jobs.models import *
from django.contrib.auth.models import User

headers = {'User-agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:61.0) Gecko/20100101 Firefox/61.0 '} #it saying that you a browser and dont get blocked as a bot


baseUrl = 'https://in.indeed.com'
url = f'https://in.indeed.com/jobs?q=mckinsey&start={page}&vjk=f3956d0aa511eb6a'
r = requests.get(url, headers)
soup = BeautifulSoup(r.content, 'html.parser')


table1 = soup.find_all('div' , class_ = 'cardOutline')
def jobScan(link): #here we will be reciving the link from a tag
    the_job = {}
    
    jobUrl = '{}{}'.format(baseUrl, link['href'])
    job = requests.get(jobUrl, headers=headers)
    jobSoup=BeautifulSoup(job,"html.parser")
    
    title = jobSoup.find_all("h1")[0].text
    the_job['title'] = title
    

        

def extract(page):
          headers = {'User-Agent' : 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.54 Safari/537.36'}
          url = f'https://in.indeed.com/jobs?q=mckinsey&start={page}&vjk=f3956d0aa511eb6a'
          r = requests.get(url, headers)
          soup = BeautifulSoup(r.content, 'html.parser')
          return soup
      


    
def transform(soup):
     
     divs = soup.find_all('div' , class_ = 'cardOutline')
      
     #return print(divs)# did to check if it is working can remove 
     for item in divs:
         title = item.find('a').text.strip()  #as this "a" is first tag
         company = item.find('span' , class_ = 'companyName' ).text.strip()
         summary = item.find('li' )
         linke = item.find("a", {"class": "jcs-JobTitle"})
         url1 = linke['href']
         #summary = item.find('div' , {'class' : 'job-snippet' }).text.strip().replace('\n' , '')  #if it is not a class then you can pass in a python dictionary here
         
         
         
         
         
         
         job = {        #this we have made to store all the information above somewhere
                'title': title,
                'company': company,
                #'salary': salary,
                'summary': summary,
                'url': url1
                
                
             
             
             
             
             }
         joblist.append(job) 
     
     return

joblist = []

final_jobs = []
for i in range(0,70,10):
    print(f'Getting page, {i}')
    c = extract(0)
#print(transform(c))   #will tell how many there are
    transform(c)
    final_jobs.append(transform(c))





#print(transform(c))   #will tell how many there are
     


the_user = User.objects.get(email='bhargava.kavya2009@gmail.com')
#the_company = Company.objects.get(uniqueId = '139266d6')
for test_job in final_jobs: #the way this is structed is that job will only fit one category
    
    if 'Director' in test_job['title']:
        the_category = Category.objects.get(title= 'Director')
    elif 'Engineer' in test_job['title']:
        the_category = Category.objects.get(title= 'Engineer')
    elif 'Developer' in test_job['title']:
        the_category = Category.objects.get(title= 'Developer')
    elif 'Databases' in test_job['title']:
        the_category = Category.objects.get(title= 'Databases')
    elif 'Business Development' in test_job['title']:
        the_category = Category.objects.get(title= 'Business Development')
    elif 'Technology' in test_job['title']:
        the_category = Category.objects.get(title= 'Technology')
    elif 'Research' in test_job['title']:
        the_category = Category.objects.get(title= 'Research')
    elif 'Trainee' in test_job['title']:
        the_category = Category.objects.get(title= 'Trainee')
    elif 'Specialist' in test_job['title']:
        the_category = Category.objects.get(title= 'Specialist')
    elif 'Manager' in test_job['title']:
        the_category = Category.objects.get(title= 'Manager')
    else:
        the_category = Category.objects.get(title= 'Uncategorised')
    
    newjob = Jobs.objects.create(
        title = test_job['title'],
        location = test_job['location'],
        date_posted = date.today(),
        type = test_job['type'],
        contract_type = test_job['contract_type'],
        urlLink = test_job['url'],
       # company = the_company,
        category = the_category,
        owner = the_user,
    )