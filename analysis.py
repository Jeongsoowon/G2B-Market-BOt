import re
# 특수문자, 한글 모두 지워서 숫자로 만들어주는 함수.
def makeNum(strNum):
    new_string = re.sub(r"[^0-9]","", strNum)
    return int(new_string)