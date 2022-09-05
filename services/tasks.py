# importing modules

from __future__ import absolute_import, unicode_literals
from celery import shared_task
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from fake_useragent import UserAgent

# importing model from models.py
from jobs.models import Job
from .models import Scraping_Service
from bs4 import BeautifulSoup as beauty
import cloudscraper
import re
import logging


logging.basicConfig(
    filename="scrapping.log",
    filemode="w",
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
)


@shared_task
def start_web_scraping_indeed():
    scraper = cloudscraper.create_scraper(delay=10, browser="chrome")
    for link in Scraping_Service.objects.all():
        if link.is_active:
            if link.url_link.split(".")[1] == "indeed":
                try:
                    info = scraper.get(link.url_link).content
                except Exception:
                    logging.error("Error in getting link")
                    break
                soup = beauty(info, "html.parser")
                jobs_card = soup.find_all(
                    "div", class_="job_seen_beacon"
                )  # get all jobs cards
                for card in jobs_card:
                    # v = card.find_all("span")
                    job_title = card.find("a", id=re.compile("^job_")).find("span").text
                    company_name = card.find("span", class_="companyName").text
                    company_location = card.find("div", class_="companyLocation").text
                    job_rating = card.find("span", class_="ratingNumber")["aria-label"]
                    job_duties = card.find("div", class_="job-snippet").find("li").text
                    job_type = card.find("div", class_="attribute_snippet")
                    add = ( 
                        link.url_link.split("/")[0] + "//" + link.url_link.split("/")[2]
                    )
                    url_link = card.find("h2", class_=re.compile("^jobTitle")).find(
                        "a"
                    )["href"]
                    url_link = add + url_link
                    job_entry = Job.objects.create(
                        title=job_title,
                        company=company_name,
                        location=company_location,
                        rating=job_rating,
                        duties=job_duties,
                        contract_type=job_type,
                        url_link=url_link,
                    )
                    job_entry.save()
                    logging.info(f"{job_entry.id} {job_title} has been added to the database")
        else:
            logging.info(f"{link.url_link} is not active")
