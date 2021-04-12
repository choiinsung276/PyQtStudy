from PyQt5.QtCore import QDate , Qt, QTime, QDateTime
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow

now = QDate.currentDate()
print(now.toString())
print(now.toString('d.M.yy'))
print(now.toString('dd.MM.yyyy'))
print(now.toString(Qt.ISODate))
print(now.toString(Qt.DefaultLocaleLongDate))
print("=============================")

time = QTime.currentTime()
print(time.toString())
print(time.toString('h.m.s'))
print(time.toString('hh.mm.ss'))
print(time.toString(Qt.DefaultLocaleLongDate))
print(time.toString(Qt.DefaultLocaleShortDate))

print("---------------")
dt = QDateTime.currentDateTime()
print(dt.toString('d.M.yy hh:mm:ss'))
print(dt.toString('dd.MM.yyyy, hh:mm:ss'))
print(dt.toString(Qt.DefaultLocaleLongDate))
print(dt.toString(Qt.DefaultLocaleShortDate))

class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.date=QDate.currentDate()
        self.initUI()

    def initUI(self):
        self.statusBar().showMessage(self.date.toString(Qt.DefaultLocaleLongDate))
        self.setWindowTitle('Date')
        self.setGeometry(300,300,400,200)
        self.show()

if __name__=='__main__':
    app=QApplication(sys.argv)
    ex=MyApp()
    sys.exit(app.exec_())