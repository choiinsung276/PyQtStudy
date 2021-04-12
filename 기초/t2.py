import sys 
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QIcon

class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Icon')
        #self.setWindowIcon(QIcon('/img/web.jpg'))
        self.setWindowIcon(QIcon('web.jpg'))
        # x, y 창의 위치 결정 , 뒤의 두 매개변수는 너비와 높이 
        self.setGeometry(300,300,300,200)
        self.show()

if __name__=='__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())