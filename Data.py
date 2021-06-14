"""
    최근 몇개월 간 특정 지역의 공사 정보를 리스트에 저장함.
"""


from search import searchTask
# 연도, 월, 일 입력 // '일' 은 반드시 같게 해주세요!
start = [2020, 6, 14]
end = [2021, 6, 14]
check, count = False, 0
result = []
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
    
    print(tempStart, tempEnd)
   
   
    result.extend(searchTask('공사', '강원', '조경시설물설치공사업', '강원도 횡성군', tempStart, tempEnd))

    if check:
        break
    


print(result)
   