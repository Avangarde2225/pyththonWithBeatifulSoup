from bs4 import BeautifulSoup
import requests

html_text = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation=').text
soup = BeautifulSoup(html_text,'lxml')
jobs = soup.find_all('li', class_ = 'clearfix job-bx wht-shd-bx')

for job in jobs:
    publish_date = job.find('span', class_='sim-posted').span.text
    if 'few' in publish_date:
#jobs = soup.find('li', class_ = 'clearfix job-bx wht-shd-bx')
        company_name = job.find('h3', class_='joblist-comp-name').text.replace(' ', '')
        skills = job.find('span', class_='srp-skills').text.replace(' ', '')

        print(f"Company Name : {company_name.strip()}")
        print(f"Required Skills : {skills.strip()}")
        print('')

          




