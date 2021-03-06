from bs4 import BeautifulSoup
import requests
import time


def find_jobs():
    html_text = requests.get(
        'https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation=').text
    soup = BeautifulSoup(html_text, 'lxml')
    jobs = soup.find_all('li', class_='clearfix job-bx wht-shd-bx')

    for job in jobs:
        publish_date = job.find('span', class_='sim-posted').span.text
        if 'few' in publish_date:
            # jobs = soup.find('li', class_ = 'clearfix job-bx wht-shd-bx')
            company_name = job.find('h3', class_='joblist-comp-name').text.replace(' ', '')
            skills = job.find('span', class_='srp-skills').text.replace(' ', '')
            more_info: job.header.h2.a['href']

            print(f"Company Name : {company_name.strip()}")
            print(f"Required Skills : {skills.strip()}")
            print(f"Link to the Job : {more_info}")
            print('')

if __name__ == '__main__':
    while True:
        find_jobs()
        time_wait = 10
        print(f'Waiting {time_wait} seconds...')
        time.sleep(time_wait * 60)



