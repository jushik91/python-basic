import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *


class Form(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUI()



    def setupUI(self):
        self.setWindowTitle("Test")

        self.setGeometry(400,200,500,500)

        btn_1=QPushButton('Click1', self)
        btn_2=QPushButton('Click2', self)
        btn_3=QPushButton('Click3', self)

        btn_1.move(30,30)
        btn_2.move(30,60)
        btn_3.move(30,90)


        ##이벤트 : 위젯을 투르면 연결해서 실해항는 것
        btn_1.clicked.connect(self.btn_1_clicked)

        btn_2.clicked.connect(self.btn_2_clicked)

        btn_3.clicked.connect(QCoreApplication.instance().quit)




    ##슬롯 : 윗젯을 동작시키는 함수
    def btn_1_clicked(self):
        QMessageBox.about(self,'message','clicked')

    def btn_2_clicked(self):
        print('Button2 Clikced !!!!!!!!')









###########################################

if __name__ == '__main__':
    app=QApplication(sys.argv)

    window=Form()
    window.show()
    app.exec_()
