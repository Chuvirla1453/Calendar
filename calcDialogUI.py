# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'calcDialogUI.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_CalcDialog(object):
    def setupUi(self, CalcDialog):
        CalcDialog.setObjectName("CalcDialog")
        CalcDialog.resize(273, 250)
        self.tabWidget = QtWidgets.QTabWidget(CalcDialog)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 271, 121))
        self.tabWidget.setObjectName("tabWidget")
        self.dateTab = QtWidgets.QWidget()
        self.dateTab.setObjectName("dateTab")
        self.label = QtWidgets.QLabel(self.dateTab)
        self.label.setGeometry(QtCore.QRect(20, 20, 81, 21))
        self.label.setObjectName("label")
        self.comboBox = QtWidgets.QComboBox(self.dateTab)
        self.comboBox.setGeometry(QtCore.QRect(20, 60, 81, 21))
        self.comboBox.setObjectName("comboBox")
        self.dateEdit = QtWidgets.QDateEdit(self.dateTab)
        self.dateEdit.setGeometry(QtCore.QRect(140, 20, 121, 21))
        self.dateEdit.setObjectName("dateEdit")
        self.dayLine = QtWidgets.QLineEdit(self.dateTab)
        self.dayLine.setGeometry(QtCore.QRect(140, 60, 121, 21))
        self.dayLine.setObjectName("dayLine")
        self.warning_lbl = QtWidgets.QLabel(self.dateTab)
        self.warning_lbl.setGeometry(QtCore.QRect(140, 80, 121, 16))
        self.warning_lbl.setStyleSheet("color: rgb(255, 0, 0);")
        self.warning_lbl.setText("")
        self.warning_lbl.setObjectName("warning_lbl")
        self.tabWidget.addTab(self.dateTab, "")
        self.intervalTab = QtWidgets.QWidget()
        self.intervalTab.setObjectName("intervalTab")
        self.label_2 = QtWidgets.QLabel(self.intervalTab)
        self.label_2.setGeometry(QtCore.QRect(10, 30, 41, 21))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.intervalTab)
        self.label_3.setGeometry(QtCore.QRect(10, 70, 41, 16))
        self.label_3.setObjectName("label_3")
        self.dateEdit1 = QtWidgets.QDateEdit(self.intervalTab)
        self.dateEdit1.setGeometry(QtCore.QRect(80, 30, 131, 21))
        self.dateEdit1.setObjectName("dateEdit1")
        self.dateEdit2 = QtWidgets.QDateEdit(self.intervalTab)
        self.dateEdit2.setGeometry(QtCore.QRect(80, 70, 131, 21))
        self.dateEdit2.setObjectName("dateEdit2")
        self.tabWidget.addTab(self.intervalTab, "")
        self.result_lbl = QtWidgets.QLabel(CalcDialog)
        self.result_lbl.setGeometry(QtCore.QRect(10, 170, 241, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setKerning(False)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.result_lbl.setFont(font)
        self.result_lbl.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.result_lbl.setText("")
        self.result_lbl.setTextFormat(QtCore.Qt.AutoText)
        self.result_lbl.setObjectName("result_lbl")
        self.addButton = QtWidgets.QPushButton(CalcDialog)
        self.addButton.setGeometry(QtCore.QRect(80, 210, 111, 31))
        self.addButton.setObjectName("addButton")
        self.calcButton = QtWidgets.QPushButton(CalcDialog)
        self.calcButton.setGeometry(QtCore.QRect(80, 130, 111, 31))
        self.calcButton.setObjectName("calcButton")

        self.dateEdit.setDate(QtCore.QDate().currentDate())
        self.dateEdit1.setDate(QtCore.QDate().currentDate())
        self.dateEdit2.setDate(QtCore.QDate().currentDate())
        self.comboBox.addItems(['????????????', '??????????'])

        self.retranslateUi(CalcDialog)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(CalcDialog)

    def retranslateUi(self, CalcDialog):
        _translate = QtCore.QCoreApplication.translate
        CalcDialog.setWindowTitle(_translate("CalcDialog", "?????????????? ????????"))
        self.label.setText(_translate("CalcDialog", "????????????"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.dateTab), _translate("CalcDialog", "????????"))
        self.label_2.setText(_translate("CalcDialog", "??"))
        self.label_3.setText(_translate("CalcDialog", "????"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.intervalTab), _translate("CalcDialog", "????????????????"))
        self.addButton.setText(_translate("CalcDialog", "???????????????? ????????????"))
        self.calcButton.setText(_translate("CalcDialog", "????????????????????"))
