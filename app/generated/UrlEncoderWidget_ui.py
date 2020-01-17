# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'resources/views/UrlEncoderWidget.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_UrlEncoderWidget(object):
    def setupUi(self, UrlEncoderWidget):
        UrlEncoderWidget.setObjectName("UrlEncoderWidget")
        UrlEncoderWidget.resize(595, 492)
        self.verticalLayout = QtWidgets.QVBoxLayout(UrlEncoderWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.txt_source = QtWidgets.QPlainTextEdit(UrlEncoderWidget)
        self.txt_source.setObjectName("txt_source")
        self.verticalLayout.addWidget(self.txt_source)
        self.frame = QtWidgets.QFrame(UrlEncoderWidget)
        self.frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setLineWidth(0)
        self.frame.setObjectName("frame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.btn_url_encode = QtWidgets.QPushButton(self.frame)
        self.btn_url_encode.setObjectName("btn_url_encode")
        self.horizontalLayout.addWidget(self.btn_url_encode)
        self.btn_url_decode = QtWidgets.QPushButton(self.frame)
        self.btn_url_decode.setObjectName("btn_url_decode")
        self.horizontalLayout.addWidget(self.btn_url_decode)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.verticalLayout.addWidget(self.frame)
        self.txt_target = QtWidgets.QPlainTextEdit(UrlEncoderWidget)
        self.txt_target.setReadOnly(True)
        self.txt_target.setObjectName("txt_target")
        self.verticalLayout.addWidget(self.txt_target)

        self.retranslateUi(UrlEncoderWidget)
        QtCore.QMetaObject.connectSlotsByName(UrlEncoderWidget)

    def retranslateUi(self, UrlEncoderWidget):
        _translate = QtCore.QCoreApplication.translate
        UrlEncoderWidget.setWindowTitle(_translate("UrlEncoderWidget", "Form"))
        self.txt_source.setPlainText(_translate("UrlEncoderWidget", "http://www.google.com"))
        self.btn_url_encode.setText(_translate("UrlEncoderWidget", "Url Encode"))
        self.btn_url_decode.setText(_translate("UrlEncoderWidget", "Url Decode"))

