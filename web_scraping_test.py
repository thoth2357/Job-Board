# from pprint import pprint
import requests
# import cloudscraper
# import re
from bs4 import BeautifulSoup as beauty

url = 'https://in.indeed.com/jobs?q=mckinsey&start=0&vjk=9346afd4052633e7'
url2 = 'https://www.linkedin.com/jobs/search/?currentJobId=3187861296&geoId=102713980&keywords=mckinsey&location=India&refresh=true'

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
# print(len(jobs))
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
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.chrome.options import Options
# from webdriver_manager.chrome import ChromeDriverManager
# from fake_useragent import UserAgent

# from bs4 import BeautifulSoup as beauty
# import re

# chrome_options = Options()
# chrome_options.headless = False
# # ua = UserAgent(use_cache_server=False, verify_ssl=False)
# # chrome_options.add_argument(f'user-agent={ua.chrome}')

# driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
# driver.get(url)
# page_source = driver.page_source

# soup = beauty(page_source, 'html.parser')
# # print(soup)

# # scraping for indeed link given for companies
# jobs_card = soup.find_all('div', class_='job_seen_beacon') #get all jobs cards
# company_logo = soup.find('div', class_='univsrch-ci-logo-small').find('img')['src']
# print(company_logo)
# # get all job spans
# jobs_card_span = soup.find_all('span', class_='jobtitle')
# for card in jobs_card:
#             v=card.find_all('span')
#             # print(v)
#             #univsrch-ci > div.univsrch-ci-block > div.univsrch-ci-logo-small > a > img
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
#             break
