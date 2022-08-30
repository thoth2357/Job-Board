from pprint import pprint
import cloudscraper
from bs4 import BeautifulSoup as beauty

url = 'https://in.indeed.com/jobs?q=mckinsey&start=0&vjk=9346afd4052633e7'


scraper = cloudscraper.create_scraper(delay=10, browser='chrome') 
info  = scraper.get(url).content
soup = beauty(info, 'html.parser')
# pprint(soup.prettify())



