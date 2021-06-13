import pyautogui

#특정 위치를 찾기 위한 코드
screenWidth, screenHeight = pyautogui.size()

print('{0} , {1}'.format(screenWidth, screenHeight))

while(1):
    check = int(input('끝내려면 1, 확인하려면 2를 입력하세요.! '))
    x, y = pyautogui.position()
    if check == 2 :
        print(x, y)
        check == 0
    if check == 1: 
        break
