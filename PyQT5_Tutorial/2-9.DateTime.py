# 현재 날짜 출력
print('현재 날짜 출력')
from PyQt5.QtCore import QDate

now = QDate.currentDate()
print(now.toString())

# 날짜 형식 설정
print('\n날짜 형식 설정하기')
from PyQt5.QtCore import QDate, Qt

now = QDate.currentDate()
print(now.toString('d.M.yy'))
print(now.toString('dd.MM.yyyy'))
print(now.toString('ddd.MMMM.yyyy'))
print(now.toString(Qt.ISODate))
print(now.toString(Qt.DefaultLocaleLongDate))

# 현재 시간 출력
print('\n현재 시간 출력')
from PyQt5.QtCore import QTime

time = QTime.currentTime()
print(time.toString())

# 시간 형식 설정
print('\n시간 형식 설정')
from PyQt5.QtCore import QTime, Qt

time = QTime.currentTime()
print(time.toString('h.m.s'))
print(time.toString('hh.mm.ss'))
print(time.toString('hh.mm.ss.zzz'))
print(time.toString(Qt.DefaultLocaleLongDate))
print(time.toString(Qt.DefaultLocaleShortDate))

# 현재 날짜와 시간 출력
print('\n현재 날짜와 시간 출력')
from PyQt5.QtCore import QDateTime

datetime = QDateTime.currentDateTime()
print(datetime.toString())

# 날짜와 시간 형식 설정
print('\n날짜와 시간 형식 설정')
from PyQt5.QtCore import QDateTime, Qt

datetime = QDateTime.currentDateTime()
print(datetime.toString('d.M.yy hh:mm:ss'))
print(datetime.toString('dd.MM.yyyy, hh:mm:ss'))
print(datetime.toString(Qt.DefaultLocaleLongDate))
print(datetime.toString(Qt.DefaultLocaleShortDate))
print()

# 상태 표시줄에 날짜 표시
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtCore import QDate, Qt


class MyApp(QMainWindow):

    def __init__(self):
        super().__init__()

        self.date = QDate.currentDate()
        self.initUI()

    def initUI(self):

        self.statusBar().showMessage(self.date.toString(Qt.DefaultLocaleLongDate))

        self.setWindowTitle('Date')
        self.setGeometry(300, 300, 400, 200)
        self.show()


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())