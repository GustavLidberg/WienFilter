# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\Gustav\Desktop\Projektkurs\Code\src\pythion\_layout\input.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Input(object):
    def setupUi(self, Input):
        Input.setObjectName("Input")
        Input.resize(172, 95)
        self.frame = QtWidgets.QFrame(Input)
        self.frame.setGeometry(QtCore.QRect(10, 10, 151, 71))
        self.frame.setFrameShape(QtWidgets.QFrame.Box)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.frame)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 131, 51))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.nameLabel = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.nameLabel.setText("")
        self.nameLabel.setObjectName("nameLabel")
        self.verticalLayout.addWidget(self.nameLabel)
        self.inputLCD = QtWidgets.QLCDNumber(self.verticalLayoutWidget)
        self.inputLCD.setStyleSheet("color: rgb(255, 0, 0);")
        self.inputLCD.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.inputLCD.setProperty("value", 0.0)
        self.inputLCD.setProperty("intValue", 0)
        self.inputLCD.setObjectName("inputLCD")
        self.verticalLayout.addWidget(self.inputLCD)

        self.retranslateUi(Input)
        QtCore.QMetaObject.connectSlotsByName(Input)

    def retranslateUi(self, Input):
        _translate = QtCore.QCoreApplication.translate
        Input.setWindowTitle(_translate("Input", "Input Device"))
