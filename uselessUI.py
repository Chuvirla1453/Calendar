# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'uselessUI.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_UselessDialog(object):
    def setupUi(self, UselessDialog):
        UselessDialog.setObjectName("UselessDialog")
        UselessDialog.resize(444, 467)
        self.textEdit = QtWidgets.QTextEdit(UselessDialog)
        self.textEdit.setGeometry(QtCore.QRect(10, 20, 421, 361))
        self.textEdit.setObjectName("textEdit")
        self.saveButton = QtWidgets.QPushButton(UselessDialog)
        self.saveButton.setGeometry(QtCore.QRect(30, 400, 171, 31))
        self.saveButton.setObjectName("saveButton")
        self.cancelButton = QtWidgets.QPushButton(UselessDialog)
        self.cancelButton.setGeometry(QtCore.QRect(240, 400, 171, 31))
        self.cancelButton.setObjectName("cancelButton")

        self.retranslateUi(UselessDialog)
        QtCore.QMetaObject.connectSlotsByName(UselessDialog)

    def retranslateUi(self, UselessDialog):
        _translate = QtCore.QCoreApplication.translate
        UselessDialog.setWindowTitle(_translate("UselessDialog", "Заметки"))
        self.saveButton.setText(_translate("UselessDialog", "Сохранить"))
        self.cancelButton.setText(_translate("UselessDialog", "Отменить изменения"))