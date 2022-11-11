# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './src/layout/xml/output.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Output(object):
    def setupUi(self, Output):
        Output.setObjectName("Output")
        Output.resize(182, 309)
        self.verticalLayoutWidget = QtWidgets.QWidget(Output)
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

        self.retranslateUi(Output)
        QtCore.QMetaObject.connectSlotsByName(Output)

    def retranslateUi(self, Output):
        _translate = QtCore.QCoreApplication.translate
        Output.setWindowTitle(_translate("Output", "Output Device"))
        self.label.setText(_translate("Output", "Voltage Supply"))
        self.label_2.setText(_translate("Output", "(last set target value)"))
        self.label_3.setText(_translate("Output", "(new target value)"))
        self.setBtn.setText(_translate("Output", "Set value"))
