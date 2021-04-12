import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QHBoxLayout, QVBoxLayout

class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        okButton = QPushButton('OK')
        cancelButton = QPushButton('Cancel')
        okButton1 = QPushButton('OK1')
        okButton2 = QPushButton('OK2')
        okButton3 = QPushButton('OK3')
        okButton4 = QPushButton('OK4')
        okButton5 = QPushButton('OK5')
        okButton6 = QPushButton('OK6')
        okButton7 = QPushButton('OK7')
        hbox2 = QHBoxLayout()
        hbox2.addStretch(4)
        hbox2.addWidget(okButton1)
        hbox2.addWidget(okButton2)
        hbox2.addWidget(okButton3)
        hbox2.addWidget(okButton4)
        hbox2.addWidget(okButton5)
        hbox2.addStretch(1)

        hbox = QHBoxLayout()
        hbox.addStretch(1)
        hbox.addWidget(okButton)
        hbox.addWidget(cancelButton)
        hbox.addStretch(1)

        vbox = QVBoxLayout()
        vbox.addStretch(3)
        vbox.addLayout(hbox)
        vbox.addStretch(3)
        vbox.addWidget(okButton6)
        vbox.addWidget(okButton7)
        vbox.addLayout(hbox2)
        vbox.addStretch(1)

        self.setLayout(vbox)

        self.setWindowTitle('Box Layout')
        self.setGeometry(300,100,1500,900)
        self.show()

if __name__=='__main__':
    app=QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())