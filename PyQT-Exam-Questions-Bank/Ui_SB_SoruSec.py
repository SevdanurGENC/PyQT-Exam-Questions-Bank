# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'd:\pyqt5\ExamQuestion\SB_SoruSec.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_SB_SoruSec(object):
    def setupUi(self, SB_SoruSec):
        SB_SoruSec.setObjectName("SB_SoruSec")
        SB_SoruSec.resize(1470, 508)
        self.centralwidget = QtWidgets.QWidget(SB_SoruSec)
        self.centralwidget.setObjectName("centralwidget")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(10, 10, 1441, 401))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(950, 420, 501, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(10, 420, 931, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        SB_SoruSec.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(SB_SoruSec)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1470, 22))
        self.menubar.setObjectName("menubar")
        SB_SoruSec.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(SB_SoruSec)
        self.statusbar.setObjectName("statusbar")
        SB_SoruSec.setStatusBar(self.statusbar)

        self.retranslateUi(SB_SoruSec)
        QtCore.QMetaObject.connectSlotsByName(SB_SoruSec)

    def retranslateUi(self, SB_SoruSec):
        _translate = QtCore.QCoreApplication.translate
        SB_SoruSec.setWindowTitle(_translate("SB_SoruSec", "Soru Bankasından Soru Seçimi"))
        self.pushButton.setText(_translate("SB_SoruSec", "YAZDIR"))
        self.pushButton_2.setText(_translate("SB_SoruSec", "YAZDIRILACAK SORU BANKASINA AIT DOSYAYI SECINIZ"))
