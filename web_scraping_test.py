# from pprint import pprint
from datetime import datetime, timedelta
import re
import requests
import time
# import cloudscraper
# import re
from bs4 import BeautifulSoup as beauty

url = 'https://in.indeed.com/jobs?q=mckinsey&start=0&vjk=9346afd4052633e7'
url2 = 'https://www.linkedin.com/jobs/search/?currentJobId=3187861296&geoId=102713980&keywords=mckinsey&location=India&refresh=true'
url3 = 'https://in.indeed.com/viewjob?jk=e65622a1d40c94ee&from=serp&vjs=3'

url4 = 'https://in.indeed.com/jobs?q=mckinsey&start=0&vjk=d25cab40526ba5f6'
url5 = "https://in.indeed.com/jobs?q=google&start=0&vjk=d25cab40526ba5f6" #test one
url6 = "https://ng.indeed.com/jobs?q=python+developer&l=Lagos&vjk=d39780ce052454c7"
# # response = requests.get(url)
  
# # print(response)
	
# # soup = beauty(response.content,'html.parser')
# scraper = cloudscraper.create_scraper(
#         disableCloudflareV1 = True,
#         delay=30, 
#         browser={
#             'browser': 'chrome',
#             'platform': 'windows',
#             'mobile': False
#         }
#     ) 
# info  = scraper.get(url).content
# soup = beauty(info, 'html.parser')
# print(soup)

# # scraping for indeed link given for companies
# jobs_card = soup.find_all('div', class_='job_seen_beacon') #get all jobs cards
# company_logo = soup.find('div', class_='univsrch-ci-logo-small')
# print(company_logo)
# #get all job spans
# jobs_card_span = soup.find_all('span', class_='jobtitle')
# for card in jobs_card:
#             v=card.find_all('span')
#             # print(v)
#             print(card.find("a",id=re.compile("^job_")).find('span').text)
#             print("\n")
#             print(card.find('span',class_ = "companyName").text)
#             print("\n")
#             print(card.find('div',class_="companyLocation").text)
#             print("\n")
#             print(card.find('span', class_="ratingNumber")['aria-label'])
#             print("\n")
#             print(card.find('div', class_="job-snippet").find('li').text)
#             print("\n")
#             print(card.find('h2', class_=re.compile("^jobTitle")).find('a')['href'])
# '''
# span 1 = job title  -> to find use that jobTitle exists in id
# span 2 = company name -> use span class of companyName
# span 3 = rating -> use span class of ratingNumber
# to get company location make use of div class of companyLocation in the loop
# date posted - > 
# for job snippet look for div class of job-snippet and get li under it for snippet
# this is done and tested code snippet is below
# for card in jobs_card:
#             v=card.find_all('span')
#             print(card.find("span",id=re.compile("^jobTitle-")))
#             print("\n")
#             print(card.find('span',class_ = "companyName"))
#             print("\n")
#             print(card.find('div',class_="companyLocation"))
#             print("\n")
#             print(card.find('span', class_="ratingNumber")['aria-label'])
#             print("\n")
#             print(card.find('div', class_="job-snippet").find('li'))
#             break
# '''
# # jobs_card_span = soup.find('div', id="ember240")
# # print(jobs_card_span)

# -----------------------------------------------------------------------------------------linkedin
# response = requests.get(url2)
# soup = beauty(response.content, "html.parser")
# jobs = soup.find_all('div', class_='base-card relative w-full hover:no-underline focus:no-underline base-card--link base-search-card base-search-card--link job-search-card')
# # print(len(jobs))
# for job in jobs:
#     job_title = job.find('h3', class_='base-search-card__title').text.strip()
#     job_company = job.find('h4', class_='base-search-card__subtitle').text.strip()
#     job_location = job.find('span', class_='job-search-card__location').text.strip()
#     job_link = job.find('a', class_='base-card__full-link')['href']
#     job_company_logo = job.find('div', class_='search-entity-media').find('img')['data-delayed-url']

#     print(job_title)
#     print(job_company)
#     print(job_location)
#     print(job_link)
#     print(job_company_logo)
#     print("\n")

#     response2 = requests.get(job_link)
#     time.sleep(5)
    
#     # print(response2)
#     soup2 = beauty(response2.content,'html.parser')
#     # requirement = soup2.find('div', class_='description__text description__text--rich').find('ul').find_all('li')
#     # requirement = [i.text for i in requirement]
#     # print(requirement)
    
#     requirement = soup2.find('div', class_='description__text description__text--rich').text
#     qualifications_index = requirement.index('Qualifications')
#     duties_index = requirement.index('What You\'ll Do')
#     pager_index = requirement.index('Show more')
#     qualifications = requirement[qualifications_index:duties_index]
#     duties = requirement[duties_index:pager_index].strip()
#     category = soup2.find_all('span',class_='description__job-criteria-text description__job-criteria-text--criteria')[2].text.strip()
#     contract_type = soup2.find_all('span',class_='description__job-criteria-text description__job-criteria-text--criteria')[1].text.strip()
#     date_posted = soup2.find('span',class_='posted-time-ago__text topcard__flavor--metadata').text.strip()
#     # print('date_posted', date_posted)
#     if 'day' in date_posted:
#         timer = 1
#     elif 'week' in date_posted:
#         timer = 7
#     elif 'month' in date_posted:
#         timer = 30
#     elif 'year' in date_posted:
#         timer = 365
#     else:
#         timer = 1
#     count_of_time = int(re.findall(r'[0-9]', date_posted)[0])
#     total_time_elapsed = count_of_time * timer
#     date_job_posted_datetime = datetime.now() - timedelta(days=total_time_elapsed)
#     # print('date_job_posted_datetime', date_job_posted_datetime)
#     print(qualifications)
#     print('\n')
#     print(duties)
#     print('\n')
#     print(contract_type)
#     print('\n')
#     print(category)
#     print("\n")
#     break

# -----------------------------------------------------------------------------------indeed
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from fake_useragent import UserAgent
from time import sleep

from bs4 import BeautifulSoup as beauty
import re

chrome_options = Options()
# chrome_options.add_argument('--remote-debugging-port=9222')
chrome_options.headless = False
chrome_options.add_argument("--incognito")
# ua = UserAgent(use_cache_server=False, verify_ssl=False)
# chrome_options.add_argument(f'user-agent={ua.chrome}')

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
driver.get(url5)
sleep(20)
page_source = driver.page_source


soup = beauty(page_source, 'html.parser')
# print(soup)

# scraping for indeed link given for companies
jobs_card = soup.find_all('div', class_='job_seen_beacon') #get all jobs cards
# company_logo = soup.find('div', class_='univsrch-ci-logo-small')
# print(company_logo)
# get all job spans
jobs_card_span = soup.find_all('span', class_='jobtitle')
for card in jobs_card:
            v=card.find_all('span')
            # print(v)
            #univsrch-ci > div.univsrch-ci-block > div.univsrch-ci-logo-small > a > img
            print(card.find("a",id=re.compile("^job_")).find('span').text)
            print("\n")
            print(card.find('span',class_ = "companyName").text)
            print("\n")
            print(card.find('div',class_="companyLocation").text)
            print("\n")
            print(card.find('span', class_="ratingNumber")['aria-label'])
            print("\n")
            print(card.find('div', class_="job-snippet").find('li').text)
            print("\n")
            print(card.find('h2', class_=re.compile("^jobTitle")).find('a')['href'])
            
            add = (
                        url5.split("/")[0] + "//" + url5.split("/")[2]
                    )
            url_link = card.find("h2", class_=re.compile("^jobTitle")).find("a")["href"]
                    
            url_link_new = add + url_link
                    
            print(url_link_new)
            driver.get(url_link_new)
            sleep(20)
            full_job_qualifications_duties = driver.find_element(By.XPATH, '//*[@id="jobDescriptionText"]').text
            # qualifications = driver.find_element(By.XPATH, '//*[@id="jobDescriptionText"]/div/div[3]/div/div')
            # duties = driver.find_element(By.XPATH, '//*[@id="jobDescriptionText"]/div/div[2]')
            # date_job_posted = driver.find_element(By.XPATH, '//*[@id="hiringInsightsSectionRoot"]/p/span[2]').text
            # date_number = re.findall('[0-9]+', date_job_posted)
            # date_job_posted_datetime = datetime.now() - timedelta(days=int(date_number[0]))
            # print(duties.text, qualifications.text)
            
            # company_profile = driver.find_element(By.XPATH, '//*[@id="viewJobSSRRoot"]/div[2]/div/div[3]/div/div/div[1]/div[1]/div[2]/div[1]/div[2]/div/div/div/div[1]/div[2]/div/a').get_attribute('href')
            # driver.get(company_profile)
            # sleep(10)
            # company_logo = driver.find_element(By.XPATH, '//*[@id="cmp-container"]/div/div[1]/header/div[2]/div[3]/div/div/div/div[1]/div[1]/div[1]/div/div/img').get_attribute('src')
            # print('comapany logo',company_logo)
            # print('job date',date_job_posted_datetime)
            print('full job qualifications and duties',full_job_qualifications_duties)
            break
        
driver.close()