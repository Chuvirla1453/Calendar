# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'addDialogUI.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_editDialog(object):
    def setupUi(self, addDialog):
        addDialog.setObjectName("addDialog")
        addDialog.resize(402, 278)
        self.label = QtWidgets.QLabel(addDialog)
        self.label.setGeometry(QtCore.QRect(20, 80, 131, 21))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(addDialog)
        self.label_2.setGeometry(QtCore.QRect(20, 130, 131, 21))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(addDialog)
        self.label_3.setGeometry(QtCore.QRect(20, 20, 111, 31))
        self.label_3.setObjectName("label_3")
        self.fullTimeWidget = QtWidgets.QWidget(addDialog)
        self.fullTimeWidget.setGeometry(QtCore.QRect(140, 130, 241, 31))
        self.fullTimeWidget.setObjectName("fullTimeWidget")
        self.dateTimeEdit = QtWidgets.QDateTimeEdit(self.fullTimeWidget)
        self.dateTimeEdit.setGeometry(QtCore.QRect(13, 0, 221, 31))
        self.dateTimeEdit.setObjectName("dateTimeEdit")
        self.incompleteTimeWidget = QtWidgets.QWidget(addDialog)
        self.incompleteTimeWidget.setGeometry(QtCore.QRect(140, 129, 241, 31))
        self.incompleteTimeWidget.setObjectName("incompleteTimeWidget")
        self.dateEdit = QtWidgets.QDateEdit(self.incompleteTimeWidget)
        self.dateEdit.setGeometry(QtCore.QRect(13, 0, 221, 31))
        self.dateEdit.setObjectName("dateEdit")
        self.typeBox = QtWidgets.QComboBox(addDialog)
        self.typeBox.setGeometry(QtCore.QRect(150, 80, 231, 31))
        self.typeBox.setObjectName("typeBox")
        self.titleLine = QtWidgets.QLineEdit(addDialog)
        self.titleLine.setGeometry(QtCore.QRect(150, 20, 231, 31))
        self.titleLine.setObjectName("titleLine")
        self.completedWidget = QtWidgets.QWidget(addDialog)
        self.completedWidget.setGeometry(QtCore.QRect(20, 180, 361, 41))
        self.completedWidget.setObjectName("completedWidget")
        self.label_4 = QtWidgets.QLabel(self.completedWidget)
        self.label_4.setGeometry(QtCore.QRect(0, 10, 101, 21))
        self.label_4.setObjectName("label_4")
        self.completedCheckBox = QtWidgets.QCheckBox(self.completedWidget)
        self.completedCheckBox.setGeometry(QtCore.QRect(130, 10, 70, 17))
        self.completedCheckBox.setObjectName("completedCheckBox")
        self.editButton = QtWidgets.QPushButton(addDialog)
        self.editButton.setGeometry(QtCore.QRect(120, 240, 131, 23))
        self.editButton.setObjectName("addButton")
        self.warninglbl = QtWidgets.QLabel(addDialog)
        self.warninglbl.setGeometry(QtCore.QRect(150, 55, 201, 16))
        self.warninglbl.setStyleSheet("color: rgb(255, 0, 0);")
        self.warninglbl.setText("")
        self.warninglbl.setObjectName("warninglbl")

        self.retranslateUi(addDialog)
        QtCore.QMetaObject.connectSlotsByName(addDialog)

    def retranslateUi(self, addDialog):
        _translate = QtCore.QCoreApplication.translate
        addDialog.setWindowTitle(_translate("addDialog", "?????????????????????????? ????????????"))
        self.label.setText(_translate("addDialog", "?????? ??????????????:"))
        self.label_2.setText(_translate("addDialog", "?????????? ????????????????????:"))
        self.label_3.setText(_translate("addDialog", "????????????????:"))
        self.label_4.setText(_translate("addDialog", "???????????????????"))
        self.completedCheckBox.setText(_translate("addDialog", "????/??????"))
        self.editButton.setText(_translate("addDialog", "??????????????????????????"))
