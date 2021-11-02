import sqlite3
import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPixmap
from mainUI import Ui_MainWindow
from addDialogUI import Ui_addDialog
from editDialogUI import Ui_editDialog
import datetime as dt
import time

DATES = []

class CustomCalendar(QtWidgets.QCalendarWidget):
    def __init__(self, parent=None):
        QtWidgets.QCalendarWidget.__init__(self, parent)
        time.sleep(0.1)
        self.why_are_you_not_working()

    def paintCell(self, painter, rect, date):
        global DATES
        QtWidgets.QCalendarWidget.paintCell(self, painter, rect, date)
        t = date.getDate()
        if date in DATES or QtCore.QDate(1918, t[1], t[2]) in DATES:
            painter.setPen(QtGui.QPen(QtGui.QColor(179, 255, 102), 2, Qt.SolidLine, Qt.RoundCap))
            painter.drawLine(rect.topRight(), rect.topLeft())
            painter.drawLine(rect.topRight(), rect.bottomRight())
            painter.drawLine(rect.bottomLeft(), rect.bottomRight())
            painter.drawLine(rect.topLeft(), rect.bottomLeft())
        elif date == date.currentDate():
            painter.setBrush(QtGui.QColor(255, 159, 159, 50))
            painter.setPen(QtGui.QColor(0, 0, 0, 0))
            painter.drawRect(rect)

    def why_are_you_not_working(self):
        global DATES
        con = sqlite3.connect('entry_db.db')
        cur = con.cursor()
        dates = cur.execute("SELECT date FROM times")
        DATES = []
        for i in dates:
            i = i[0].split('-')
            DATES.append(QtCore.QDate(int(i[0]), int(i[1]), int(i[2])))



class MainWindow(QMainWindow, Ui_MainWindow):
    def setupUI(self, MainWindow):
        self.setupUi(self)
        MainWindow.setFixedSize(835, 640)
        MainWindow.move(542, 0)

        self.image = QLabel(self)
        self.image.resize(1, 1)
        self.image.move(0, 0)

    def __init__(self):
        super().__init__()
        self.setupUI(self)
        self.setFixedSize(835, 640)

        self.update_calendar()

        self.mainCalendar.clicked.connect(self.date_clicked)

        self.con = sqlite3.connect('entry_db.db')
        self.cur = self.con.cursor()

        self.addButton.clicked.connect(self.create_add_dialog)
        self.editButton.clicked.connect(self.create_edit_dialog)
        self.delButton.clicked.connect(self.create_del_dialog)

    def update_calendar(self):
        self.mainCalendar = CustomCalendar(self.centralwidget)
        self.mainCalendar.setGeometry(QtCore.QRect(0, 0, 831, 621))
        self.mainCalendar.setObjectName("mainCalendar")

    def update_result(self, date_in):
        cur = self.cur
        date = f"{date_in[0]}-{'0' * (2 - len(str(date_in[1]))) + str(date_in[1])}" \
               f"-{'0' * (2 - len(str(date_in[2]))) + str(date_in[2])}"
        self.date = date
        gen_date = f"1918-{'0' * (2 - len(str(date_in[1]))) + str(date_in[1])}" \
                   f"-{'0' * (2 - len(str(date_in[2]))) + str(date_in[2])}"
        result = cur.execute(f"""SELECT type_id, time_id, entry, completed FROM main_data WHERE time_id in
         (SELECT id FROM times WHERE date = '{date}' or date = '{gen_date}')""").fetchall()
        if not result:
            return 0
        self.entryTable.setRowCount(len(result) + 1)
        self.entryTable.setColumnCount(len(result[0]))
        self.titles = [description[0] for description in cur.description]

        self.types = {}
        for i in cur.execute("SELECT * FROM types").fetchall():
            self.types[i[0]] = (i[1], i[2])

        self.times = {}
        for i in cur.execute("SELECT id, time FROM times").fetchall():
            self.times[i[0]] = i[1]

        for i in range(len(result[0])):
            self.entryTable.setItem(0, i, QTableWidgetItem({0: 'Тип записи', 1: 'Время', 2: 'Название', 3: 'Статус'}[i]))
        for i, elem in enumerate(result):
            for j, val in enumerate(elem):
                if j == 0:
                    val = self.types[val][0]
                    s = self.types[3] == 1
                elif j == 1:
                    val = self.times[val]
                    t = val
                    if val == None:
                        val = 'Весь день'
                elif j == 3:
                    a = [int(i) for i in str(dt.date.today()).split('-')]
                    b = [int(i) for i in date.split('-')]

                    val = {None: 'Не закончено', 0: 'Не закончено', 1: 'Закончено', 'NONE': 'Не закончено'}[val]

                    if val == 'Не закончено':
                        if dt.datetime(a[0], a[1], a[2]) > dt.datetime((lambda x:
                        QtCore.QDate(2021, 11, 30).currentDate().getDate()[0] if x == 1918 else x)(b[0]), b[1], b[2]):
                            if not s or t == None:
                                val = 'Закончено'
                            else:
                                val = 'Просрочено'
                        elif s and t == None:
                            pass
                        elif s and t != None:
                            c = [int(i) for i in t.split(':')]
                            if dt.time(c[0], c[1], 0) < dt.datetime.now().time():
                                val = 'Просрочено'

                self.entryTable.setItem(i + 1, j, QTableWidgetItem(str(val)))
        return 1

    def date_clicked(self, date):
        if type(date) == tuple:
            t = date
        else:
            t = date.getDate()
        self.setFixedSize(835, 915)
        self.curDate.setText(QtCore.QDate(t[0], t[1], t[2]).toString())
        if not self.update_result(t):
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

    def create_add_dialog(self):
        self.dialog = AddDialog(self, self.date)
        self.dialog.show()

    def create_edit_dialog(self, entry):
        self.dialog = 3
        self.dialog.show()

    def create_del_dialog(self):
        rows = list(set([i.row() for i in self.entryTable.selectedItems()]))
        if not rows:
            self.statusBar().showMessage('Ничего не выбрано')
            return 0
        types = self.cur.execute(f"""SELECT id FROM types WHERE title IN 
        ('{"', '".join([self.entryTable.item(i, 0).text() for i in rows])}')""").fetchall()[0]

        times = self.cur.execute(f"""SELECT id FROM times WHERE time IN 
        ('{"', '".join([self.entryTable.item(i, 1).text() for i in rows])}') AND date = '{self.date}'""").fetchall()[0]

        entries = [self.entryTable.item(i, 2).text() for i in rows]
        status = [self.entryTable.item(i, 3).text() for i in rows]

        ids = self.cur.execute(f"""SELECT id FROM main_data WHERE type_id IN ({', '.join([str(i) for i in list(types)])})
         AND time_id IN ({', '.join([str(i) for i in list(times)])}) AND entry IN ('{"', '".join(entries)}')""").fetchall()[0]
        valid = QMessageBox.question(
            self, '', "Вы действительно хотите удалить выбранные записи",
            QMessageBox.Yes, QMessageBox.No)
        if valid == QMessageBox.Yes:
            cur = self.con.cursor()
            cur.execute(f"""DELETE FROM times WHERE id IN ({', '.join([str(i) for i in list(times)])})""")
            cur.execute(f"""DELETE FROM main_data WHERE id IN ({', '.join([str(i) for i in list(ids)])})""")
            self.con.commit()
            t = self.date.split('-')
            self.date_clicked((int(t[0]), int(t[1]), int(t[2])))
            self.update_calendar()

    def mousePressEvent(self, event):
        if event.y() not in range(640, 916):
            self.setFixedSize(835, 640)


class AddDialog(QDialog, Ui_addDialog):
    def __init__(self, parent, date_in):
        super(AddDialog, self).__init__(parent)
        self.parent = parent
        self.setupUi(self)
        self.date_in = date_in
        date = date_in.split('-')

        self.dateEdit.setDate(QtCore.QDate(int(date[0]), int(date[1]), int(date[2])))
        self.dateTimeEdit.setDateTime(QtCore.QDateTime(QtCore.QDate(int(date[0]), int(date[1]), int(date[2])), QtCore.QTime(0, 0)))

        self.con = parent.con
        self.cur = parent.cur
        self.typeBox.addItems([i[0] for i in self.cur.execute("SELECT title FROM types").fetchall()])
        self.addButton.clicked.connect(self.addToDB)
        self.typeBox.activated[str].connect(self.act)

        self.fullTimeWidget.show()
        self.incompleteTimeWidget.hide()
        self.completedWidget.show()
        self.periodic = False

    def act(self, txt):
        self.typeDB = txt
        if self.cur.execute(f"""SELECT periodic FROM types WHERE title = '{txt}'""").fetchall()[0][0] == 0:
            self.fullTimeWidget.show()
            self.incompleteTimeWidget.hide()
            self.completedWidget.show()
            self.periodic = False
        else:
            self.fullTimeWidget.hide()
            self.incompleteTimeWidget.show()
            self.completedWidget.hide()
            self.periodic = True

    def addToDB(self):
        entry = self.titleLine.text()
        type = self.typeBox.currentText()
        if self.periodic:
            date = str(self.dateEdit.date().toPyDate()).split('-')
            date = f'{date[2]}-{date[1]}-{date[0]}'
            time = 'NULL'
            cmpltd = 'NULL'
        else:
            date = str(self.dateTimeEdit.dateTime().toPyDateTime()).split()
            time = date[1][:-3]
            date = date[0]
            cmpltd = {True: 1, False: 0}[self.completedCheckBox.isChecked()]

        if not entry:
            self.warninglbl.setText('Введите название')
        else:
            self.warninglbl.setText('')
            self.cur.execute(f"""INSERT INTO times(time, date) VALUES('{time}', '{date}')""")
            self.con.commit()
            time_id = self.cur.execute(f"""SELECT id FROM times WHERE time = '{time}' AND date = '{date}'""").fetchall()[0][0]
            type_id = self.cur.execute(f"""SELECT id FROM types WHERE title = '{type}'""").fetchall()[0][0]
            self.cur.execute(f"""INSERT INTO main_data(type_id, time_id,
             entry, completed) VALUES({type_id}, {time_id}, '{entry}', {cmpltd})""")
            self.con.commit()
            self.parent.statusBar().showMessage('Запись успешно добавлена')
            self.parent.date_clicked(tuple(map(int, date.split('-'))))
            self.close()
            self.parent.update_calendar()


class EditDialog(QDialog, Ui_editDialog):
    pass


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainWindow()
    ex.show()
    exit(app.exec())