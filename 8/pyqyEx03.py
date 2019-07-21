import sys
from PyQt5.QtWidgets import *
from PyQt5 import QtWidgets,QtCore

class Form(QMainWindow):
    def __init__(self):

        super().__init__()
        self.setupUI()


    def setupUI(self):

        self.setWindowTitle('Test3')
        self.setGeometry(200,200,300,400)


        label_1=QLabel('입력1',self)

        label_2=QLabel('입력2',self)

        label_1.move(20,20)

        label_2.move(20,60)

        self.lineEdit = QLineEdit('',self)
        self.plainEdit=QtWidgets.QPlainTextEdit(self)

        self.lineEdit.move(90,20)

        self.plainEdit.setGeometry(QtCore.QRect(20,90,200,150))

        self.statusBar = QStatusBar(self)
        self.setStatusBar(self.statusBar)


        ##이벤트를 넣자
        self.lineEdit.textChanged.connect(self.lineEditChanged)

        self.lineEdit.returnPressed.connect(self.lineEditEnter)





    def lineEditChanged(self):
        self.statusBar.showMessage(self.lineEdit.text())


    def lineEditEnter(self):
        self.plainEdit.appendPlainText(self.lineEdit.text())
        self.lineEdit.clear()


if __name__=='__main__':
    app=QApplication(sys.argv)
    window=Form()
    window.show()
    app.exec_()
