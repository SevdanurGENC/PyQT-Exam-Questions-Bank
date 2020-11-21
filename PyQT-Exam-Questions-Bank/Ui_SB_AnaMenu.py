# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'd:\pyqt5\ExamQuestion\SB_AnaMenu.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_SB_AnaMenu(object):
    def setupUi(self, SB_AnaMenu):
        SB_AnaMenu.setObjectName("SB_AnaMenu")
        SB_AnaMenu.resize(477, 239)
        self.centralwidget = QtWidgets.QWidget(SB_AnaMenu)
        self.centralwidget.setObjectName("centralwidget")
        SB_AnaMenu.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(SB_AnaMenu)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 477, 22))
        self.menubar.setObjectName("menubar")
        self.menuIslem = QtWidgets.QMenu(self.menubar)
        self.menuIslem.setObjectName("menuIslem")
        SB_AnaMenu.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(SB_AnaMenu)
        self.statusbar.setObjectName("statusbar")
        SB_AnaMenu.setStatusBar(self.statusbar)
        self.actionYeni_Soru_Ekle = QtWidgets.QAction(SB_AnaMenu)
        self.actionYeni_Soru_Ekle.setObjectName("actionYeni_Soru_Ekle")
        self.actionSoru_Sec = QtWidgets.QAction(SB_AnaMenu)
        self.actionSoru_Sec.setObjectName("actionSoru_Sec")
        self.menuIslem.addAction(self.actionYeni_Soru_Ekle)
        self.menuIslem.addAction(self.actionSoru_Sec)
        self.menubar.addAction(self.menuIslem.menuAction())

        self.retranslateUi(SB_AnaMenu)
        QtCore.QMetaObject.connectSlotsByName(SB_AnaMenu)

    def retranslateUi(self, SB_AnaMenu):
        _translate = QtCore.QCoreApplication.translate
        SB_AnaMenu.setWindowTitle(_translate("SB_AnaMenu", "Soru Bankasi"))
        self.menuIslem.setTitle(_translate("SB_AnaMenu", "Islem"))
        self.actionYeni_Soru_Ekle.setText(_translate("SB_AnaMenu", "Yeni Soru Ekle"))
        self.actionSoru_Sec.setText(_translate("SB_AnaMenu", "Soru Sec"))
