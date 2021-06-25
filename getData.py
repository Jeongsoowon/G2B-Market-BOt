"""
    2021년 6월 25일 금요일
    원정수 (waterpurifier@khu.ac.kr)
    
    나라장터 입찰 데이터
    함수 : 
    ### v1 : 모든 기능을 통합! 
"""
from selenium import webdriver
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
