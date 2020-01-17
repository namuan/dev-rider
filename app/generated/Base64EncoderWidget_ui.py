# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'resources/views/Base64EncoderWidget.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Base64EncoderWidget(object):
    def setupUi(self, Base64EncoderWidget):
        Base64EncoderWidget.setObjectName("Base64EncoderWidget")
        Base64EncoderWidget.resize(595, 492)
        self.verticalLayout = QtWidgets.QVBoxLayout(Base64EncoderWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.txt_source = QtWidgets.QPlainTextEdit(Base64EncoderWidget)
        self.txt_source.setObjectName("txt_source")
        self.verticalLayout.addWidget(self.txt_source)
        self.frame = QtWidgets.QFrame(Base64EncoderWidget)
        self.frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setLineWidth(0)
        self.frame.setObjectName("frame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.btn_b64_encode = QtWidgets.QPushButton(self.frame)
        self.btn_b64_encode.setObjectName("btn_b64_encode")
        self.horizontalLayout.addWidget(self.btn_b64_encode)
        self.btn_b64_decode = QtWidgets.QPushButton(self.frame)
        self.btn_b64_decode.setObjectName("btn_b64_decode")
        self.horizontalLayout.addWidget(self.btn_b64_decode)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.verticalLayout.addWidget(self.frame)
        self.txt_target = QtWidgets.QPlainTextEdit(Base64EncoderWidget)
        self.txt_target.setReadOnly(True)
        self.txt_target.setObjectName("txt_target")
        self.verticalLayout.addWidget(self.txt_target)

        self.retranslateUi(Base64EncoderWidget)
        QtCore.QMetaObject.connectSlotsByName(Base64EncoderWidget)

    def retranslateUi(self, Base64EncoderWidget):
        _translate = QtCore.QCoreApplication.translate
        Base64EncoderWidget.setWindowTitle(_translate("Base64EncoderWidget", "Form"))
        self.txt_source.setPlainText(_translate("Base64EncoderWidget", "Some text"))
        self.btn_b64_encode.setText(_translate("Base64EncoderWidget", "Base64 Encode"))
        self.btn_b64_decode.setText(_translate("Base64EncoderWidget", "Base64 Decode"))

