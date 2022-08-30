from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
# from services.tasks import Scraper

# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'jobWebsite.settings')

app = Celery('jobWebsite') 
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks() # Load task modules from all registered Django app configs.

# # Scraper = Scraper()


# @app.task(bind=True)
# def debug_task(self):
#     print('Request: {0!r}'.format(self.request))

# @app.task(name='Scraping_Service Task For Indeed.com')
# def start_scrapping_service_indeed(url_link):
#     #call function to start scraper from tasks
#     print('we are in indeed')
#     pass

# @app.task(name='Scraping_Service Task For LinkedIn.com')
# def start_scrapping_service_linkedin(url_link):
#     #call function to start scraper from tasks
#     print('we are in linkedin')
#     pass