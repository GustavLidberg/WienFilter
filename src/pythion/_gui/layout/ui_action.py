# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\Gustav\Desktop\Projektkurs\Code\src\pythion\_gui\layout\action.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Action(object):
    def setupUi(self, Action):
        Action.setObjectName("Action")
        Action.resize(204, 89)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Action.sizePolicy().hasHeightForWidth())
        Action.setSizePolicy(sizePolicy)
        Action.setMinimumSize(QtCore.QSize(204, 89))
        self.button = QtWidgets.QPushButton(Action)
        self.button.setGeometry(QtCore.QRect(10, 10, 181, 21))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button.sizePolicy().hasHeightForWidth())
        self.button.setSizePolicy(sizePolicy)
        self.button.setObjectName("button")
        self.initiatedLabel = QtWidgets.QLabel(Action)
        self.initiatedLabel.setGeometry(QtCore.QRect(10, 40, 181, 16))
        self.initiatedLabel.setText("")
        self.initiatedLabel.setObjectName("initiatedLabel")
        self.finishedLabel = QtWidgets.QLabel(Action)
        self.finishedLabel.setGeometry(QtCore.QRect(10, 60, 181, 16))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.finishedLabel.sizePolicy().hasHeightForWidth())
        self.finishedLabel.setSizePolicy(sizePolicy)
        self.finishedLabel.setMinimumSize(QtCore.QSize(121, 16))
        self.finishedLabel.setStyleSheet("color: green;")
        self.finishedLabel.setText("")
        self.finishedLabel.setObjectName("finishedLabel")

        self.retranslateUi(Action)
        QtCore.QMetaObject.connectSlotsByName(Action)

    def retranslateUi(self, Action):
        _translate = QtCore.QCoreApplication.translate
        Action.setWindowTitle(_translate("Action", "Input Device"))
        self.button.setText(_translate("Action", "PushButton"))