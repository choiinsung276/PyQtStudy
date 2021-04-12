import sys
from PyQt5.QtWidgets import QApplication, QWidget, QCheckBox ,QLabel, QVBoxLayout
from PyQt5.QtCore import Qt

class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        cb = QCheckBox('박스입니다.',self)
        cb.move(20,20)
        cb.toggle()
        cb.stateChanged.connect(self.changeTitle)

        self.setWindowTitle('안녕하세요')
        self.setGeometry(300,300,300,200)
        self.show()

    def changeTitle(self,state):
        if state ==Qt.Checked:
            self.setWindowTitle('체크박스켰네요.')
            label1 = QLabel('First Label', self)
            label1.setAlignment(Qt.AlignCenter)

            label2 = QLabel('Second Label', self)
            label2.setAlignment(Qt.AlignVCenter)

            font1 = label1.font()
            font1.setPointSize(20)

            font2 = label2.font()
            font2.setFamily('Times New Roman')
            font2.setBold(True)

            label1.setFont(font1)
            label2.setFont(font2)

            layout=QVBoxLayout()
            layout.addWidget(label1)
            layout.addWidget(label2)

            self.setLayout(layout)
            
        else:
            self.setWindowTitle(' ')

if __name__=='__main__':
    app=QApplication(sys.argv)
    ex=MyApp()
    sys.exit(app.exec_())