### G2B 나라장터 검색 봇

2021년 6월 13일 
Selenium을 활용해서 만들라 했는데, 생각보다 쉽지 않았다.. element를 못읽더라니깐? 네이버에서는 잘되는데,,, <br>
그래서 확장성은 상당히 낮지만,,, width, height = 1440, 900 이면 상당히 잘 이용할 것이라 생각한다. <br>
공사, 조경식재, 강원지역 선택 후 검색하는 기능까지 구현. <br>

2021년 6월 14일 
search.py 의 공사 검색 함수를 이용하여 Data.py에서 기간 상관없이 공사목록을 저장할 수 있게되었다. <br>
-> 추가해야 할 것. 날짜에서 '일'이 겹치는 현상이 있다. <br> 
현재 귀찮기도하고 어려울 것 같아서 아직 안만들었으니 만들도록 하자! <br>

참고 : http://hleecaster.com/narajangteo-crawling/ (파이썬으로 나라장터 입찰공고 크롤링하기) <br>

2021년 6월 15일 <br>
PyQt5 로 UI를 제작할려고 했다.. <br>
이제 DataFrame 형태로 입찰결과를 볼 수 있다. (BiddingList)<br>
workList 로 공사목록을 확인 할 수 있다. <br>



--> Django, MySQL 등 잘 골라서 DB를 겹치지 않게 저장하고 자동으로 업데이트되게 하고 싶다! <br>
--> 속도가 조금 느려서 데이터 크롤링 그 부분을 수정해야 할 것 같다.



<br> <br> <br>

# 데이터 분석
<br> 21.06.19 Analysis.ipynb
<br> 이제 공고번호-차수 를 통해 원하는 입찰의 개찰결과를 볼 수 있다.
<br> 21.06.21 MySQL.ipynb update
<br> cron 사용하여 자동으로 업데이트 되게 하고싶음.
<br> 21.06.22 MySQL.ipynb update
<br> 기초금액이 누락되어 [공고번호, 기초금액] table에 추가하였음.
<br> 더 만들고 싶었으나,, Data.py 건들이다가 이상하게 되어버려서,,,, 고치는데만 시간다씀,,,,,, ㅠㅠ 
<br> 21.06.23 MySQL.ipynb, Data.py, Analysis.ipynb, Analysis.py Update
<br> biddingList에 치명적 오류발생,,, 공고번호가 맞지않는 상황이 생겨서 고치느라 오늘 하루 다씀,,,, 이래서 차분히 코딩하면서 오류가 없는지 하나하나 <br> 점검 했어야했는데,,
<br> 여튼,, 고치진 못했고,, 기초금액이 필요한 상태였기에 biddingList 끝자락에 넣어줬다.. <br> Analysis.py 를 통해 Analysis를 진행할려고한다! 화이팅! 내일은 분석이라도 끝내자!
