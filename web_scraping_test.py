from pprint import pprint
import cloudscraper
from bs4 import BeautifulSoup as beauty
import re

url = 'https://in.indeed.com/jobs?q=mckinsey&start=0&vjk=9346afd4052633e7'


scraper = cloudscraper.create_scraper(delay=10, browser='chrome') 
info  = scraper.get(url).content
soup = beauty(info, 'html.parser')


#scraping for indeed link given for companies
jobs_card = soup.find_all('div', class_='job_seen_beacon') #get all jobs cards

#get all job spans
jobs_card_span = soup.find_all('span', class_='jobtitle')
for card in jobs_card:
            v=card.find_all('span')
            print(card.find("span",id=re.compile("^jobTitle-")))
            print("\n")
            print(card.find('span',class_ = "companyName"))
            print("\n")
            print(card.find('div',class_="companyLocation"))
            print("\n")
            print(card.find('span', class_="ratingNumber")['aria-label'])
            print("\n")
            print(card.find('div', class_="job-snippet").find('li'))
            break
'''
span 1 = job title  -> to find use that jobTitle exists in id
span 2 = company name -> use span class of companyName
span 3 = rating -> use span class of ratingNumber
to get company location make use of div class of companyLocation in the loop
date posted - > 
for job snippet look for div class of job-snippet and get li under it for snippet
this is done and tested code snippet is below
for card in jobs_card:
            v=card.find_all('span')
            print(card.find("span",id=re.compile("^jobTitle-")))
            print("\n")
            print(card.find('span',class_ = "companyName"))
            print("\n")
            print(card.find('div',class_="companyLocation"))
            print("\n")
            print(card.find('span', class_="ratingNumber")['aria-label'])
            print("\n")
            print(card.find('div', class_="job-snippet").find('li'))
            break
'''

