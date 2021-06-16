"""
    최근 몇개월 간 특정 지역의 공사 정보를 리스트에 저장함. (workList)
    입찰 결과까지 저장함. (BiddingList)
"""

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from search import searchTask
import pandas as pd
from collections import deque

def parse_G2B():
    # 연도, 월, 일 입력 // '일' 은 반드시 같게 해주세요!
    start = [2020, 6, 14]
    end = [2021, 6, 14]
    check, count = False, 0
    workList = []
    while True:
        if count == 0:
            tempStart = start
            # 5개월 간격으로 검색.
            tempEnd = [start[0], start[1] + 5, start[2]]
            if tempEnd[1] > 12:
                tempEnd[0] += 1
                tempEnd[1] -= 12
            count += 1
        else:
            tempStart = [int(tempEnd[0]), int(tempEnd[1]), int(tempEnd[2])]
            print(tempEnd)
            tempEnd = [tempStart[0], tempStart[1] + 5, tempStart[2]]
            if tempEnd[1] > 12:
                tempEnd[0] += 1
                tempEnd[1] -= 12
            if tempEnd[0] == end[0] and tempEnd[1] == end[1]:
                check = True
            elif tempEnd[0] == end[0] and tempEnd[1] > end[1]:
                tempEnd[1] = end[1]
                check = True
       
        workList.extend(searchTask('공사', '강원', '조경시설물설치공사업', '강원도 횡성군', tempStart, tempEnd))

        if check or count == 1: # 수정해야함.!
            break


    try:
        driver = webdriver.Chrome('/Users/waterpurifier/Downloads/chromedriver')
        BiddingList = []

        for result in workList:
            driver.get(result[2])
            driver.find_element_by_xpath('//*[@id="container"]/div[24]/table/tbody/tr/td[5]/a/span').click()
            elem = driver.find_element_by_class_name('results')
            div_list = elem.find_elements_by_tag_name('div')
            biddingResult = []
            for div in div_list:
                biddingResult.append(div.text)

            BiddingList.append([biddingResult[i * 9:(i + 1) * 9] for i in range((len(biddingResult) + 9 - 1)// 9)])

        return workList, BiddingList
    except Exception as e:
        # 위 코드에서 에러가 발생한 경우 출력
        print(e)
    finally:
        # 에러와 관계없이 실행되고, 크롬 드라이버를 종료
        driver.quit()

workList, BiddingList = parse_G2B()
# data Frame 생성. 
df = pd.DataFrame(columns=['공고번호-차수', '순위', '사업자 등록번호', '업체명', '대표자명', '입찰금액(원)', '투찰률(%)', '추첨 번호', '투찰일시', '비고'])
count = 0
for idx in range(len(BiddingList)):
    for j in BiddingList[idx]:
        temp = deque(j)
        temp.appendleft(workList[idx][1])
        df.loc[count] = list(temp)
        count += 1

print(df)