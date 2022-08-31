from pprint import pprint
import cloudscraper
from bs4 import BeautifulSoup as beauty

url = 'https://in.indeed.com/jobs?q=mckinsey&start=0&vjk=9346afd4052633e7'


scraper = cloudscraper.create_scraper(delay=10, browser='chrome') 
info  = scraper.get(url).content
soup = beauty(info, 'html.parser')


#scraping for indeed link given for companies
jobs_card = soup.find_all('div', class_='job_seen_beacon') #get all jobs cards

#get all job spans
jobs_card_span = soup.find_all('span', class_='jobtitle')