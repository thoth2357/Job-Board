# importing modules
from celery import shared_task
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

from bs4 import BeautifulSoup as beauty
import re
import requests
import logging
import time
from datetime import datetime, timedelta

from jobs.models import Job
from .models import Scraping_Service


logging.basicConfig(
    filename="scrapping.log",
    filemode="w",
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
)

chrome_options = Options()
chrome_options.headless = False


@shared_task
def start_web_scraping_indeed():
    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()), options=chrome_options
    )
    for link in Scraping_Service.objects.all():
        if link.is_active:
            if link.url_link.split(".")[1] == "indeed":
                try:
                    driver.get(link.url_link)
                    time.sleep(20)
                    page_source = driver.page_source
                except Exception:
                    logging.error("Error in getting link")
                    break
                soup = beauty(page_source, "html.parser")
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
                    
                    url_link_new = add + url_link
                    
                    print(url_link_new)
                    driver.get(url_link_new)
                    time.sleep(10)
                    qualifications = driver.find_element(By.XPATH, '//*[@id="jobDescriptionText"]/div/div[3]/div/div').text
                    job_duties = driver.find_element(By.XPATH, '//*[@id="jobDescriptionText"]/div/div[2]').text
                    date_job_posted = driver.find_element(By.XPATH, '//*[@id="hiringInsightsSectionRoot"]/p/span[2]').text
                    date_number = re.findall('[0-9]+', date_job_posted)
                    if date_number and len(date_number) >= 1:
                        date_job_posted_datetime = datetime.now() - timedelta(days=int(date_number[0]))
                    else:
                        date_job_posted_datetime = datetime.now()
                    company_profile = driver.find_element(By.XPATH, '//*[@id="viewJobSSRRoot"]/div[2]/div/div[3]/div/div/div[1]/div[1]/div[2]/div[1]/div[2]/div/div/div/div[1]/div[2]/div/a').get_attribute('href')
                    driver.get(company_profile)
                    time.sleep(10)
                    company_logo = driver.find_element(By.XPATH, '//*[@id="cmp-container"]/div/div[1]/header/div[2]/div[3]/div/div/div/div[1]/div[1]/div[1]/div/div/img').get_attribute('src')
                    job_entry = Job.objects.create(
                        title=job_title,
                        logo=company_logo,
                        company=company_name,
                        location=company_location,
                        rating=job_rating,
                        duties=job_duties,
                        requirements = qualifications,
                        contract_type=job_type,
                        url_link=url_link,
                        source="Indeed",
                        date_posted = date_job_posted_datetime,
                    )
                    job_entry.save()
                    logging.info(
                        f"{job_entry.id} {job_title} has been added to the database"
                    )
        else:
            logging.info(f"{link.url_link} is not active")


@shared_task
def start_web_scraping_linkedin():
    """
    function to use to start webscraping tasks
    """
    for link in Scraping_Service.objects.all():
        if link.is_active:
            if link.url_link.split(".")[1] == "linkedin":
                try:
                    response = requests.get(link.url_link)
                    soup = beauty(response.content, "html.parser")
                    jobs = soup.find_all(
                        "div",
                        class_="base-card relative w-full hover:no-underline focus:no-underline base-card--link base-search-card base-search-card--link job-search-card",
                    )
                    for job in jobs:
                        job_title = job.find(
                            "h3", class_="base-search-card__title"
                        ).text.strip()
                        job_company = job.find(
                            "h4", class_="base-search-card__subtitle"
                        ).text.strip()
                        job_location = job.find(
                            "span", class_="job-search-card__location"
                        ).text.strip()
                        job_link = job.find("a", class_="base-card__full-link")["href"]
                        job_company_logo = job.find(
                            "div", class_="search-entity-media"
                        ).find("img")["data-delayed-url"]

                        response2 = requests.get(job_link)
                        soup2 = beauty(response2.content, "html.parser")

                        requirement = soup2.find(
                            "div", class_="description__text description__text--rich"
                        ).text
                        qualifications_index = requirement.index("Qualifications")
                        duties_index = requirement.index("What You'll Do")
                        pager_index = requirement.index("Show more")
                        qualifications = requirement[qualifications_index:duties_index]
                        duties = requirement[duties_index:pager_index].strip()
                        category = soup2.find_all(
                            "span",
                            class_="description__job-criteria-text description__job-criteria-text--criteria",
                        )[2].text.strip()
                        contract_type = soup2.find_all(
                            "span",
                            class_="description__job-criteria-text description__job-criteria-text--criteria",
                        )[1].text.strip()

                        job_entry = Job.objects.create(
                            title=job_title,
                            logo=job_company_logo,
                            company=job_company,
                            location=job_location,
                            duties=duties,
                            requirements=qualifications,
                            category=category,
                            contract_type=contract_type,
                            url_link=job_link,
                            source="LinkedIn",
                        )
                        job_entry.save()
                        logging.info(
                            f"{job_entry.id} {job_title} has been added to the database"
                        )
                except Exception as e:
                    logging.error(f"Error in getting link {e}")
                    break
