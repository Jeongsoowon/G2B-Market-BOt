"""
    Django 사용하기 위해 bs4 이용하여 크롤링
"""


from selenium import webdriver
from bs4 import BeautifulSoup
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "web.settings")
import django
django.setup()
def parse_blog():
    driver = webdriver.Chrome('/Users/waterpurifier/Downloads/chromedriver')
    driver.implicitly_wait(3)
    #driver.get(workList[0][2])
    driver.get('http://www.g2b.go.kr:8081/ep/invitation/publish/bidInfoDtl.do?bidno=20210610767&bidseq=00&releaseYn=Y&taskClCd=3')
    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')
    notices = soup.select('table > tbody > tr > td.tr')

    data = {}
    for n in notices:
        data['basicPrice'] = n.text() 
    return data

