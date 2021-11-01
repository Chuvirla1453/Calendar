import sqlite3
import sys
from PyQt5.QtCore import Qt
from PyQt5 import uic
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPixmap


class CustomCalendar(QtWidgets.QCalendarWidget):
    def __init__(self, parent=None):
        QtWidgets.QCalendarWidget.__init__(self, parent)
        con = sqlite3.connect('entry_db.db')
        cur = con.cursor()
        dates = cur.execute("SELECT date FROM times")
        self.dates = []
        for i in dates:
            i = i[0].split('-')
            self.dates.append(QtCore.QDate((lambda x: QtCore.QDate(2021, 11, 30).currentDate().getDate()[0]
            if x == 1918 else int(i[0]))(int(i[0])), int(i[1]), int(i[2])))

    def paintCell(self, painter, rect, date):
        QtWidgets.QCalendarWidget.paintCell(self, painter, rect, date)
        if date in self.dates:
            painter.setPen(QtGui.QPen(QtGui.QColor(179, 255, 102), 2, Qt.SolidLine, Qt.RoundCap))
            painter.drawLine(rect.topRight(), rect.topLeft())
            painter.drawLine(rect.topRight(), rect.bottomRight())
            painter.drawLine(rect.bottomLeft(), rect.bottomRight())
            painter.drawLine(rect.topLeft(), rect.bottomLeft())
        elif date == date.currentDate():
            painter.setBrush(QtGui.QColor(255, 159, 159, 50))
            painter.setPen(QtGui.QColor(0, 0, 0, 0))
            painter.drawRect(rect)


class MainWindow(QMainWindow):
    def setupUi(self, MainWindow):
        MainWindow.setFixedSize(835, 640)
        MainWindow.move(542, 0)

        self.image = QLabel(self)

        self.mainCalendar = CustomCalendar(self.centralwidget)
        self.mainCalendar.setGeometry(QtCore.QRect(0, 0, 831, 621))
        self.mainCalendar.setObjectName("mainCalendar")

    def __init__(self):
        super().__init__()
        uic.loadUi('main.ui', self)
        self.setupUi(self)
        self.setFixedSize(835, 640)
        self.mainCalendar.clicked.connect(self.date_clicked)

        self.con = sqlite3.connect('entry_db.db')
        self.cur = self.con.cursor()

    def update_result(self, date_in):
        cur = self.cur
        date = f"{date_in[0]}-{'0' * (2 - len(str(date_in[1]))) + str(date_in[1])}" \
               f"-{'0' * (2 - len(str(date_in[2]))) + str(date_in[2])}"
        gen_date = f"1918-{'0' * (2 - len(str(date_in[1]))) + str(date_in[1])}" \
                   f"-{'0' * (2 - len(str(date_in[2]))) + str(date_in[2])}"
        result = cur.execute(f"""SELECT type_id, time_id, entry, completed FROM main_data WHERE time_id in
         (SELECT id FROM times WHERE date = '{date}' or date = '{gen_date}')""").fetchall()
        if not result:
            return 0
        self.entryTable.setRowCount(len(result))
        self.entryTable.setColumnCount(len(result[0]))
        self.titles = [description[0] for description in cur.description]
        self.types = {}
        for i in cur.execute("SELECT * FROM types").fetchall():
            self.types[i[0]] = (i[1], i[2])
        self.times = {}
        for i in cur.execute("SELECT id, time FROM times").fetchall():
            self.times[i[0]] = i[1]
        for i, elem in enumerate(result):
            for j, val in enumerate(elem):
                if j == 0:
                    t = val
                    val = self.types[val][0]
                elif j == 1:
                    val = self.times[val]
                    if val == None:
                        val = 'Весь день'
                elif j == 3:
                    val = {None: '', 'FALSE': 'Не закончено', 'TRUE': 'Закончено'}[val]

                self.entryTable.setItem(i, j, QTableWidgetItem(str(val)))
        return 1

    def date_clicked(self, date):
        self.setFixedSize(835, 915)
        self.curDate.setText(date.toString())
        if not self.update_result(date.getDate()):
            self.setFixedSize(835, 1006)
            self.dateData.hide()
            self.pixmap = QPixmap('shrek.jpg')
            self.image.move(0, 653)
            self.image.resize(920, 366)
            self.image.hide()
            self.image.show()
            self.widget.show()
            self.image.setPixmap(self.pixmap)
        else:
            self.image.resize(1, 1)
            self.image.move(0, 0)
            self.image.hide()
            self.dateData.show()

    def mousePressEvent(self, event):
        if event.y() not in range(640, 916):
            self.setFixedSize(835, 640)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainWindow()
    ex.show()
    exit(app.exec())