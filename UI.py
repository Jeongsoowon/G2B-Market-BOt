import sys
from PyQt5.QtWidgets import *



# button 생성
#button = QPushButton("Button")
#button.show()

# Label 생성
#label = QLabel("Label")
#label.show()

# window 생성
class MyWindow(QMainWindow):
    def __init__(self, width, height):
        super().__init__()
        x, y = 0, 0
        # title 생성.
        self.setWindowTitle("My HTS v1.0")
        # window 크기설정
        self.setGeometry(x, y, width, height)
        # button 생성
        btn = QPushButton(text = "매수", parent=self)
        btn.move(x + 10, y + 10)

        # quit 생성
        btn_quit = QPushButton(text = "종료", parent = self)
        btn_quit.move(x + 20, y + 20)
        btn_quit.clicked.connect(self.Quit)


    def Quit(self):
        QApplication.instance().quit()        

app = QApplication(sys.argv)
width, height = 600, 800
window = MyWindow(600, 800)
window.show()
app.exec_()
