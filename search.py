"""
    나라장터 검색을 위한 html url 생성 후 목록 반환
"""


def tenderOpening(resultList, number):
    find_work = resultList['공고번호'] == number
    return resultList[find_work]

# 날짜 String으로 변환
def makeString(arg1):
    arg1[0] = str(arg1[0])
    if arg1[1] < 10:
        arg1[1] = '0' + str(arg1[1])
    else:
        arg1[1] = str(arg1[1])
    arg1[2] = str(arg1[2])
    return arg1
"""
task = 공사, 용역, 민간, 기타 중 하나를 선택.
area = 강원 중 하나를 선택
industry = 조경식재공사업, 조경시설물설치공사업
myArea = 검색결과에서 특정 지역을 골라낼때 사용
"""
def searchTask(task, area, industry, myArea, start, end):
    # 크롬 브라우저를 띄우기 위해, 웹드라이버를 가져오기
    from selenium import webdriver
    # 크롬 드라이버로 크롬을 실행한다.
    driver = webdriver.Chrome('/Users/waterpurifier/Downloads/chromedriver')
    try:
        
        # 업무 종류, 지역, 체크
        task_dict = {'공사' : '3', '용역': '5', '민간': '20', '기타': '4'}
        industryCd_dict = {'조경식재공사업' : '0023', '조경시설물설치공사업' : '0049'}
        industry_dict = {'조경식재공사업' : '%C1%B6%B0%E6%BD%C4%C0%E7%B0%F8%BB%E7%BE%F7', '조경시설물설치공사업' : '%C1%B6%B0%E6%BD%C3%BC%B3%B9%B0%BC%B3%C4%A1%B0%F8%BB%E7%BE%F7'}
        area_dict = {'강원' : '42'}
        # 검색날짜 선택 
        start = makeString(start)
        end = makeString(end)
        startYear, startMonth, startDay = start[0], start[1], start[2]
        endYear, endMonth, endDay = end[0], end[1], end[2]
       

        searchType = '1'
        bidSearchType = '1'
        # 검색 날짜
        fromBidDt = startYear + '%2F' + startMonth + '%2F' + startDay
        toBidDt = endYear + '%2F' + endMonth + '%2F' + endDay

        radOrgan = '1'
        budgetCompare ='UP'
        regYn ='Y'
        # 검색 노출 개수
        recordCountPerPage = '100'

        html = 'http://www.g2b.go.kr:8101/ep/tbid/tbidList.do?' + 'searchType=' + searchType + '&bidSearchType=' + bidSearchType + '&taskClCds=' + task_dict[task] + '&searchDtType=1' + '&fromBidDt=' + fromBidDt + '&toBidDt=' + toBidDt + '&radOrgan=' + radOrgan + '&budgetCompare=' + budgetCompare + '&regYn=' + regYn + '&recordCountPerPage=' + recordCountPerPage + '&area=' + area_dict[area] + '&industry=' + industry_dict[industry] + '&industryCd=' + industryCd_dict[industry]
        # 조건에 맞게 검색     
        driver.get(html)
        # 검색 결과 확인
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
    
    except Exception as e:
        # 위 코드에서 에러가 발생한 경우 출력
        print(e)
    finally:
        # 에러와 관계없이 실행되고, 크롬 드라이버를 종료
        driver.quit()
    
