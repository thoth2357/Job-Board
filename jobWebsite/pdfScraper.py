import requests
from bs4 import BeautifulSoup
import json

import pandas as pd

headers = {'User-agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:61.0) Gecko/20100101 Firefox/61.0 '} #it saying that you a browser and dont get blocked as a bot






        

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
         #summary = item.find('div' , {'class' : 'job-snippet' }).text.strip().replace('\n' , '')  #if it is not a class then you can pass in a python dictionary here
         
         
         
         
         
         
         job = {        #this we have made to store all the information above somewhere
                'title': title,
                'company': company,
                #'salary': salary,
                'summary': summary
                
             
             
             
             
             }
         joblist.append(job) 
     
     return

joblist = []

for i in range(0,70,10):
    print(f'Getting page, {i}')
    c = extract(0)
#print(transform(c))   #will tell how many there are
    transform(c)
    

df = pd.DataFrame(joblist)

print(df.head())


df.to_csv('mckinesy-jobs.csv')
