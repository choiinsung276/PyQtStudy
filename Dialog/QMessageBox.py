import sys
from PyQt5.QtWidgets import QApplication, QWidget, QMessageBox

class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('큐 메시지박스 예제')
        self.setGeometry(300,300,300,200)
        self.show()

    def closeEvent(self, event):
        reply = QMessageBox.question(self, '경고 메시지', '정말 끌꺼야?',
        QMessageBox.Yes|QMessageBox.No, QMessageBox.No)

        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

if __name__=='__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())