# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './gui/autogenerated/src/output_component.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(182, 309)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 160, 261))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.lastValueLCD = QtWidgets.QLCDNumber(self.verticalLayoutWidget)
        self.lastValueLCD.setStyleSheet("color: rgb(255, 0, 0);")
        self.lastValueLCD.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.lastValueLCD.setProperty("value", 0.0)
        self.lastValueLCD.setProperty("intValue", 0)
        self.lastValueLCD.setObjectName("lastValueLCD")
        self.verticalLayout.addWidget(self.lastValueLCD)
        self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.voltageDial = QtWidgets.QDial(self.verticalLayoutWidget)
        self.voltageDial.setMaximum(500)
        self.voltageDial.setObjectName("voltageDial")
        self.verticalLayout.addWidget(self.voltageDial)
        self.newValueLCD = QtWidgets.QLCDNumber(self.verticalLayoutWidget)
        self.newValueLCD.setStyleSheet("color: rgb(255, 0, 0);")
        self.newValueLCD.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.newValueLCD.setObjectName("newValueLCD")
        self.verticalLayout.addWidget(self.newValueLCD)
        self.label_3 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.setBtn = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.setBtn.setObjectName("setBtn")
        self.verticalLayout.addWidget(self.setBtn)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 182, 18))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Voltage Supply"))
        self.label_2.setText(_translate("MainWindow", "(last set target value)"))
        self.label_3.setText(_translate("MainWindow", "(new target value)"))
        self.setBtn.setText(_translate("MainWindow", "Set value"))