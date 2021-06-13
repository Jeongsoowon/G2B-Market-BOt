"""
    2021년 6월 13일 일요일
    원정수 (waterpurifier@khu.ac.kr)
    
    나라장터 입찰 데이터

    데이터 목록 : 입찰명, 


    ### v1 : selenium으로 왜 안되는지 모르겠어서 마우스 제어쪽으로 한번 신경을 옮겨봄,, 그래서 검색까지는 하게 했다! 
"""

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import pyautogui
from time import sleep
## Setup Driver | Chrome 
driver = webdriver.Chrome('/Users/waterpurifier/Downloads/chromedriver')
driver.implicitly_wait(3)

## Go to page
driver.get('http://www.g2b.go.kr/pt/menu/selectSubFrame.do?framesrc=/pt/menu/frameTgong.do?url=http://www.g2b.go.kr:8101/ep/tbid/tbidFwd.do')
driver.implicitly_wait(5)
# check Box 
pyautogui.moveTo(468, 525, duration = 1)
pyautogui.click()

# href
pyautogui.moveTo(520, 711, duration = 1)
pyautogui.click()

# choose
sleep(3)
pyautogui.scroll(-20)#782
pyautogui.moveTo(608,772, duration= 1)
pyautogui.click()
pyautogui.moveTo(563,811, duration= 1)
pyautogui.click()

# region
pyautogui.moveTo(844, 685, duration= 1)
pyautogui.click()
pyautogui.scroll(-10)
pyautogui.moveTo(796, 680, duration= 1)
pyautogui.click()

# search
sleep(2)
pyautogui.scroll(-10)
pyautogui.moveTo(580, 716, duration= 1)
pyautogui.click()
#pyautogui.scroll(-5)
#driver.implicitly_wait(10)
#checkbox = driver.find_element_by_id('budget').send_keys('123')


"""
    URL에 접근하는 api -> get('url')
    페이지 단일 element에 접근하는 api
    find_element_by_name('HTML_name')
    find_element_by_id('HTML_id')
    find_element_by_xpath('/html/body/some/xpath)
    페이지의 여러 elements에 접근하는 api
    find_element_by_css_selector('#css > div.selector')
    find_element_by_class_name('some_class_name')
    find_element_by_tag_name('h1')

"""