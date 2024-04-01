
# Dynamic Job Board Application
[![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](https://choosealicense.com/licenses/mit/)  

A job board is an online platform where employers list job vacancies and job seekers apply for positions. But what is the twist about this particular one is how we get the jobs to display , Which brings about the dynamic prefix name. 

This web application includes a automatic job scraping mechanism that scrapes job from platforms such as linkedin, medium, glassdoor or links set by the super admin.


The Frequency of how this jobs are scrapped are set by the super admin.







## Features

- User Registration and Login
- Scheduled Automatic Job Scraping
- Comprehensive Search & filtering Mechanisms
- Custom Filter tags (set by super admin)
- Comprehensive Log Reporting




## Prequsities

- Docker
- Docker Compose

## Run Locally

Clone the project

```bash
  git clone https://github.com/thoth2357/Job-board-web-application.git
```

Go to the project directory

```bash
  cd Job-board-web-application
```

Start the Application 

```bash
  docker compose up --build
```
To Create Super Admin, drop into terminal by executing the below command

```docker
docker exec -it <webserver-container-id> /bin/sh
```
Then Execute the below command in the opened docker shell to create the superadmin  

```bash
    poetry run python manage.py createsuperuser
```




## Screenshots
- Home Page
![App Screenshot](https://github.com/thoth2357/Dynamic-Job-Board-Application/blob/main/public/screenshots/Screenshot%202024-03-31%20at%2017.40.24.png)

- Job Search Page
![App Screenshot](https://github.com/thoth2357/Dynamic-Job-Board-Application/blob/main/public/screenshots/Screenshot%202024-03-31%20at%2017.40.50.png)

- Login Page
![App Screenshot](https://github.com/thoth2357/Dynamic-Job-Board-Application/blob/main/public/screenshots/Screenshot%202024-03-31%20at%2017.41.52.png)

- Admin Page
![App Screenshot](https://github.com/thoth2357/Dynamic-Job-Board-Application/blob/main/public/screenshots/Screenshot%202024-03-31%20at%2018.38.14.png)

- Admin Page (Task Scheduling Page)
![App Screenshot](https://github.com/thoth2357/Dynamic-Job-Board-Application/blob/main/public/screenshots/Screenshot%202024-03-31%20at%2018.38.14.png)

- Admin Page (Links to Scrape)
![App Screenshot](https://github.com/thoth2357/Dynamic-Job-Board-Application/blob/main/public/screenshots/Screenshot%202024-03-31%20at%2018.49.39.png)
  
## Authors
- [@thoth2357](https://www.github.com/thoth2357)

