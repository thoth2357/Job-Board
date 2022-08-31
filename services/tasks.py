#importing modules

from __future__ import absolute_import, unicode_literals
from celery import shared_task
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from fake_useragent import UserAgent

#importing model from models.py
from .models import Scraping_Service
# from jobWebsite.celery import start_scrapping_service_indeed, start_scrapping_service_linkedin

class Scraper():
    def __init__(self) -> None:
        #chrome option
        self.chrome_options = Options()
        self.chrome_options.add_argument("--window-size=1920,1080")
        self.chrome_options.headless = True
        self.chrome_options.add_argument("--disable-dev-shm-usage")
        self.chrome_options.add_argument("--no-sandbox")
        prefs = {"profile.managed_default_content_settings.images": 2}
        self.chrome_options.add_experimental_option("prefs", prefs)
        self.ua = UserAgent(use_cache_server=False)
        self.userAgent = self.ua.random
        self.chrome_options.add_argument(f'user-agent={self.userAgent}')

        self.get_url_links_from_db()

    def get_driver_headless(self):
        """
        Returns a webdriver object
        """
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=self.chrome_options)
        return self.driver

# def   


@shared_task
def start_web_scraping_indeed():
    scraper = Scraper()
    driver = scraper.get_driver_headless()
    for link in Scraping_Service.objects.all():
            if link.is_active:
                if link.url_link.split('.')[1] == 'indeed':
                    driver.get(link.url_link)
                    
                    
                
