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
    def get_driver_headless(self):
        """
        Returns a webdriver object
        """
        return webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=self.chrome_options)
    
    def get_page_source(self, driver, URL):
        """
        Returns the page source of the webpage
        """
        driver.get(URL)
        return driver.page_source

def get_url_links_from_db():
    """
    Returns all the URLs from the database
    """
    return [link for link in Scraping_Service.objects.all()]

def start_web_scraping():
    Scraper = Scraper()
    driver = Scraper.get_driver_headless()
    page_source = Scraper.get_page_source(driver, 'https://giphy.com/login')