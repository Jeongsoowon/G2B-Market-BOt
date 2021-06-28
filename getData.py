"""
    2021년 6월 25일 금요일
    원정수 (waterpurifier@khu.ac.kr)
    
    나라장터 입찰 데이터
    함수 : 
    ### v1 : 모든 기능을 통합! 
"""
from selenium import webdriver
import pandas as pd
from collections import deque

class getData:
    # task_dict : 업무 종류, area_dict : 지역, industryCd_dict : 공사 종류
    def __init__(self):
        self.task_dict = {'공사' : '3', '용역': '5', '민간': '20', '기타': '4'}
        self.industryCd_dict = {'조경식재공사업' : '0023', '조경시설물설치공사업' : '0049'}
        self.industry_dict = {'조경식재공사업' : '%C1%B6%B0%E6%BD%C4%C0%E7%B0%F8%BB%E7%BE%F7', '조경시설물설치공사업' : '%C1%B6%B0%E6%BD%C3%BC%B3%B9%B0%BC%B3%C4%A1%B0%F8%BB%E7%BE%F7'}
        self.area_dict = {'강원' : '42'}
        print('시작!')

    # x월을 날짜 String으로 변환
    # input -> int
    def makeString(self, arg):
        arg[0] = str(arg[0])
        if arg[1] < 10:
            arg[1] = '0' + str(arg[1])
        else:
            arg[1] = str(arg[1])
        if arg[2] < 10:
            arg[2] = '0' + str(arg[2])
        else:
            arg[2] = str(arg[2])
        return arg

    # 검색할 html을 반환.
    # task = 공사, 용역, 민간, 기타 중 하나를 선택.
    # area = 강원 중 하나를 선택
    # industry = 조경식재공사업, 조경시설물설치공사업
    # fromDay = 검색시작 날짜, toDay = 검색종료 날짜
    def makeHTML(self, task, area, industry, fromDay, toDay):
        start = self.makeString(fromDay)
        end = self.makeString(toDay)
        # 검색할 날짜 
        fromBidDt = start[0] + '%2F' + start[1] + '%2F' + end[2]
        toBidDt = end[0] + '%2F' + end[1] + '%2F' + end[2]
        # 한 페이지에 표시할 목록수
        recordCountPerPage = '100'
        html = 'http://www.g2b.go.kr:8101/ep/tbid/tbidList.do?' + 'searchType=1' + '&bidSearchType=1' + '&taskClCds=' + self.task_dict[task] + '&searchDtType=1' + '&fromBidDt=' + fromBidDt + '&toBidDt=' + toBidDt + '&radOrgan=1'  + '&budgetCompare=UP' + '&regYn=Y'  + '&recordCountPerPage=' + recordCountPerPage + '&area=' + self.area_dict[area] + '&industry=' + self.industry_dict[industry] + '&industryCd=' + self.industryCd_dict[industry]
        return html

    # html 읽어 현재 페이지를 크롤링.
    def returnList(self, driver, myArea):
        # 검색결과 확인
        elem = driver.find_element_by_class_name('results')
        div_list = elem.find_elements_by_tag_name('div')
        results = []
        for div in div_list:
            results.append(div.text)
            a_tags = div.find_elements_by_tag_name('a')
            if a_tags:
                for a_tag in a_tags:
                    link = a_tag.get_attribute('href')
                    results.append(link)
            # 검색결과 모음 리스트를 나의 지역의 결과 12개씩 분할하여 새로운 리스트로 저장
            result = [results[i * 12:(i + 1) * 12] for i in range((len(results) + 12 - 1)// 12) if myArea in results[i * 12:(i + 1) * 12] ]
        return result

    # 현재 페이지에서 입찰목록을 크롤링하여 결과를 반환함.
    def searchWork(self, myArea, html):
        try:
            # 크롬 브라우저를 띄우기 위해, 웹드라이버를 가져온다.
            driver = webdriver.Chrome('/Users/waterpurifier/Downloads/chromedriver')
            # 조건에 맞게 검색
            driver.get(html)
            result = []
            result.extend(self.returnList(driver, myArea))
            # 더보기가 있는지 없는지 체크함.
            try:
                morePage = driver.find_element_by_xpath('//*[@id="pagination"]/a')
                if morePage is not None:
                    print('🐱해당 페이지에 더 많은 페이지가 있습니다.🐶')
                    print(html)
            except Exception as e:
                print(e)
                pass

        except Exception as e:
            print(e)
            pass
        finally:
            driver.quit()
            return result

    # 크롤링 봇으로 해당하는 날짜의 모든 입찰목록을 반환함.
    def workListBot(self, task, area, industry, myArea, fromDay, toDay, step):
        result = []
        From = fromDay
        To = [fromDay[0], fromDay[1] + step, fromDay[2]]
        # 연도가 바뀌는 경우 설정
        if To[1] > 12:
            To[0] += 1
            To[1] -= 12
        To = [int(To[0]), int(To[1]), int(To[2])]
        searchContinue = (To[0] == toDay[0] and To[1] == toDay[1]) or (To[0] == toDay[0] and To[1] > toDay[1])
        html = self.makeHTML(task, area, industry, From, To)
        result.extend(self.searchWork(myArea, html))
        while not searchContinue:
            To = [int(To[0]), int(To[1]), int(To[2])]
            From = To
            To = [From[0], From[1] + step, From[2]]
            searchContinue = (To[0] == toDay[0] and To[1] == toDay[1]) or (To[0] == toDay[0] and To[1] > toDay[1])
            if To[1] > 12:
                To[0] += 1 
                To[1] -= 12
            html = self.makeHTML(task, area, industry, From, To)
            result.extend(self.searchWork(myArea, html))
            
            if searchContinue : break
            
        # 업무, 공고번호-차수, 분류, 공고명, 공고기관, 수요기관, 계약방법, 입력일시(입찰마감일시), 바로가기
        work = pd.DataFrame(columns=['업무', '공고번호', '분류', '공고명', '공고기관', '수요기관', '계약방법', '입력일시', '투찰' ,'바로가기'])
    
        for idx, w in enumerate(result):
            t = w[:2] + w[3:5] + w[6:10] + w[11:12]
            t.append(w[2])
            work.loc[idx] = t
            

        return work, result

    # 개찰결과를 반환.
    def bidListBot(self, driver, workList):
        bid = []
        for w in workList:
            try:
                # workList의 url 열기
                driver.get(w[2])
                # 재입찰인지 판단 후 개찰결과 페이지로 이동
                span_list = driver.find_elements_by_tag_name('span')
                re = 0
                for s in span_list:
                    if s.text == '재입찰':
                        re += 1
                script = "javascript:toDetail('3', '" + w[1][:11] +"', '00', '0', '"+ str(re)  +"', '개찰완료');"
                driver.execute_script(script)

                # 개찰결과 가져와 저장 
                elem = driver.find_element_by_class_name('results')
                div_list = elem.find_elements_by_tag_name('div')
                bidResult = []
                for div in div_list:
                    bidResult.append(div.text)
                
                bid.append([bidResult[i * 9:(i + 1) * 9] for i in range((len(bidResult) + 9 - 1)// 9)])

            except Exception as e:
                print(e)
        driver.quit()
        # 데이터프레임 형태로 저장
        bidDf = pd.DataFrame(columns=['순위', '사업자 등록번호', '업체명', '대표자명', '입찰금액', '투찰률', '추첨 번호', '투찰일시', '비고'])
        for idx, bids in enumerate(bid):
            for b in bids:
                bidDf.loc[idx] = b
        
        return bidDf
    
"""
check, count = False, 0
    workList = []
    while True:
        if count == 0:
            tempStart = start
            # add 개월 간격으로 검색.
            tempEnd = [start[0], start[1] + add, start[2]]
            if tempEnd[1] > 12:
                tempEnd[0] += 1
                tempEnd[1] -= 12
            count += 1
        else:
            tempStart = [int(tempEnd[0]), int(tempEnd[1]), int(tempEnd[2])]
            print(tempEnd)
            tempEnd = [tempStart[0], tempStart[1] + add, tempStart[2]]
            if tempEnd[1] > 12:
                tempEnd[0] += 1
                tempEnd[1] -= 12
            if tempEnd[0] == end[0] and tempEnd[1] == end[1]:
                check = True
            elif tempEnd[0] == end[0] and tempEnd[1] > end[1]:
                tempEnd[1] = end[1]
                check = True
       
        workList.extend(searchTask('공사', '강원', kind, '강원도 횡성군', tempStart, tempEnd))

        if check: # 수정해야함.!
            break
        

"""