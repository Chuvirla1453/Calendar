import sqlite3
import sys

from PyQt5 import uic
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPixmap


class MainWindow(QMainWindow):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(840, 910)
        MainWindow.move(542, 0)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.mainCalendar = QtWidgets.QCalendarWidget(self.centralwidget)
        self.mainCalendar.setGeometry(QtCore.QRect(0, 0, 831, 621))
        self.mainCalendar.setObjectName("mainCalendar")
        self.dateData = QtWidgets.QWidget(self.centralwidget)
        self.dateData.setGeometry(QtCore.QRect(0, 620, 831, 271))
        self.dateData.setObjectName("dateData")
        self.curDate = QtWidgets.QLabel(self.dateData)
        self.curDate.setGeometry(QtCore.QRect(10, 10, 141, 21))
        font = QtGui.QFont()
        font.setFamily("Script MT Bold")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.curDate.setFont(font)
        self.curDate.setObjectName("curDate")
        self.addButton = QtWidgets.QPushButton(self.dateData)
        self.addButton.setGeometry(QtCore.QRect(180, 0, 181, 31))
        self.addButton.setObjectName("addButton")
        self.editButton = QtWidgets.QPushButton(self.dateData)
        self.editButton.setGeometry(QtCore.QRect(380, 0, 181, 31))
        self.editButton.setObjectName("editButton")
        self.delButton = QtWidgets.QPushButton(self.dateData)
        self.delButton.setGeometry(QtCore.QRect(580, 0, 181, 31))
        self.delButton.setObjectName("delButton")
        self.entryTable = QtWidgets.QTableWidget(self.dateData)
        self.entryTable.setGeometry(QtCore.QRect(0, 40, 831, 231))
        self.entryTable.setObjectName("entryTable")
        self.entryTable.setColumnCount(0)
        self.entryTable.setRowCount(0)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.image = QLabel(self)
        self.image.move(0, 600)
        self.image.resize(920, 465)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "THE BEST PROJECT OF ALL TIMES AND PEOPLES"))
        self.curDate.setText(_translate("MainWindow", "CurrentDate"))
        self.addButton.setText(_translate("MainWindow", "Добавить запись"))
        self.editButton.setText(_translate("MainWindow", "Редактировать запись"))
        self.delButton.setText(_translate("MainWindow", "Удалить запись"))

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setFixedSize(835, 640)
        self.mainCalendar.clicked.connect(self.date_clicked)

    def date_clicked(self, date):
        print(date.getDate())
        self.setFixedSize(835, 915)
        self.curDate.setText(date.toString())
        if not False:
            print(1)
            self.setFixedSize(835, 1006)
            self.dateData.hide()
            self.pixmap = QPixmap('shrek.jpg')
            self.image.show()
            self.image.setPixmap(self.pixmap)

    def mousePressEvent(self, event):
        if event.y() not in range(640, 916):
            self.setFixedSize(835, 640)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainWindow()
    ex.show()
    exit(app.exec())