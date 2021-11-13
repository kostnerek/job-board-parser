import os; os.system("cls")
import selenium.webdriver as webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import Firefox
from selenium.webdriver.firefox.service import Service

from bs4 import BeautifulSoup

import json

from parseJobData import parseData

service = Service('./geckodriver.exe')
driver = Firefox(service=service)


def nfj_get_jobs(url, notify=True):
    driver.get(url)
    #gets html data and parses it to soup object
    content = driver.page_source
    soup = BeautifulSoup(content, features="lxml")
    #gets container of job offers
    #list_container = driver.find_element(By.CLASS_NAME, "list-container")
    for elem in soup.findAll('a', attrs={'class': 'posting-list-item'}):
        #get valuable data
        link = f"https://nofluffjobs.com{elem['href']}"
        job_title = elem.findAll('h3')[0].text.strip()
        company = elem.findAll('span')[0].text.strip()
        salary = elem.findAll('span')[1].text.strip()
        working_place = elem.findAll('span')[-1].text.strip()
        parseData('nfj', job_title, company, salary, working_place, link, notify)


def jjit_get_jobs(url, notify=True):
    content = driver.page_source
    soup = BeautifulSoup(content, features='lxml')
    jobs  = soup.findAll('div', attrs={'class':"css-ic7v2w"}, limit=1)
    data={}
    for elem in jobs:
        
        jobs_names = elem.findAll('div', attrs={'class':'jss224'})
        if not jobs_names:
            jobs_names = elem.findAll('div', attrs={'class':'jss219'})
        salaries   = elem.findAll('div', attrs={'class':'jss240'})
        if not salaries:
            salaries = elem.findAll('div', attrs={'class':'jss235'})
        links      = elem.findAll('a', attrs={'class':'jss214'})
        if not links:
            links = elem.findAll('a', attrs={'class':'jss209'})
        work_place = elem.findAll('div', attrs={'class':'jss231'})
        if not work_place:
            work_place = elem.findAll('div', attrs={'class':'jss226'})
        
        c=0
        for job in jobs_names:
            data[c] = {'job_title':job.text}
            #print(job.text)
            c+=1
        c=0
        for work in work_place:
            data[c]['working_place'] = work.text
            #print(work.text)
            c+=1
        c=0
        for salary in salaries:
            try:
                data[c]['salary'] = salary.text
                #print(salary.text)
            except:
                break
            c+=1
        c=0
        for link in links:
            url = link['href']
            subst = url[8:]
            company = subst[:subst.find("-")]
            data[c]['link'] = f"https://justjoin.it{url}"
            data[c]['company'] = company
            #print(company)
            c+=1
    
    for x in data:
        job = data[x]
        #print(job)
        try:
            parseData(  "jjit", 
                        job_title=job['job_title'], 
                        company=job['company'], 
                        salary=job['salary'], 
                        working_place=job['working_place'], 
                        link=job['link'],
                        print_messages=notify)
        except:
            raise Exception(f"Problem in url: {url}\nwith job: \n{job}")
            """ for x in data:
                print(data[x]) """




if __name__ == "__main__":
    data={}
    with open(f"config.json", encoding='utf8') as json_file:
        data = json.load(json_file)
    
    
    e = {x:y for (x,y) in data.items()}
    nfj = [x for x in e['nfj'].values()]
    jjit = [x for x in e['jjit'].values()]
    sj = [x for x in e['sj'].values()]
    
    for url in nfj:
        nfj_get_jobs(url, False)
    for url in jjit:
        driver.get(url)
        jjit_get_jobs(url, False)
    
    driver.quit()