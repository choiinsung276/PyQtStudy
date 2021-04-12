import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton, QLineEdit,
QInputDialog)

class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.btn = QPushButton('Dalog', self)
        self.btn.move(30, 30)
        self.btn.clicked.connect(self.showDialog)

        self.le = QLineEdit(self)
        self.le.move(120, 35)
        
        self.setWindowTitle("인풋 다이얼로그 예제")
        self.setGeometry(300,300,300,200)
        self.show()

    def showDialog(self):
        text, ok = QInputDialog.getText(self, '인풋 다이얼로그', 'Enter your name: ')

        if ok:
            self.le.setText(str(text)) #str로 해줘야함 

if __name__=='__main__':
    app=QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())