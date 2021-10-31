import sqlite3
import sys

from PyQt5 import uic
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPixmap


class MainWindow(QMainWindow):
    def setupUi(self, MainWindow):
        MainWindow.setFixedSize(835, 640)
        MainWindow.move(542, 0)

        self.image = QLabel(self)
        self.image.move(0, 600)
        self.image.resize(920, 465)

    def __init__(self):
        super().__init__()
        uic.loadUi('main.ui', self)
        self.setupUi(self)
        self.setFixedSize(835, 640)
        self.mainCalendar.clicked.connect(self.date_clicked)

        self.image = QLabel(self)
        self.image.move(0, 600)
        self.image.resize(920, 465)

    def date_clicked(self, date):
        self.setFixedSize(835, 915)
        self.curDate.setText(date.toString())
        if not False:
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
