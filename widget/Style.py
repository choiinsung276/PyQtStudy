import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout

class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()


    def initUI(self):
        lblred=QLabel('Red')
        lblgreen=QLabel('Green')
        lblblue=QLabel('Blue')

        lblred.setStyleSheet("color:red;"
                             "border-style:solid;"
                             "border-width: 2px;"
                             "border-color: #FA8072;"
                             "border-radius:3px")
        lblgreen.setStyleSheet("color:green;"
                               "background-color:#7FFFD4")
        lblblue.setStyleSheet("color:blue;"
                              "background-color: #87CEFA;"
                              "border-style:dashed;"
                              "border-width: 3px;"
                              "border-color: #1E90FF")

        vbox = QVBoxLayout()
        vbox.addWidget(lblred)
        vbox.addWidget(lblgreen)
        vbox.addWidget(lblblue)

        self.setLayout(vbox)

        self.setWindowTitle('Stylesheet')
        self.setGeometry(300,300,300,200)
        self.show()

if __name__=='__main__':
    app=QApplication(sys.argv)
    ex=MyApp()
    sys.exit(app.exec_())