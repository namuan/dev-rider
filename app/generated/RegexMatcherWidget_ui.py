# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'resources/views/RegexMatcherWidget.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_RegexMatcherWidget(object):
    def setupUi(self, RegexMatcherWidget):
        RegexMatcherWidget.setObjectName("RegexMatcherWidget")
        RegexMatcherWidget.resize(700, 637)
        self.verticalLayout = QtWidgets.QVBoxLayout(RegexMatcherWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame = QtWidgets.QFrame(RegexMatcherWidget)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout.setContentsMargins(12, 12, 12, 12)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btn_load_file = QtWidgets.QPushButton(self.frame)
        self.btn_load_file.setObjectName("btn_load_file")
        self.horizontalLayout.addWidget(self.btn_load_file)
        self.line = QtWidgets.QFrame(self.frame)
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.horizontalLayout.addWidget(self.line)
        self.txt_regex = QtWidgets.QLineEdit(self.frame)
        self.txt_regex.setObjectName("txt_regex")
        self.horizontalLayout.addWidget(self.txt_regex)
        self.btn_match_regex = QtWidgets.QPushButton(self.frame)
        self.btn_match_regex.setObjectName("btn_match_regex")
        self.horizontalLayout.addWidget(self.btn_match_regex)
        self.line_2 = QtWidgets.QFrame(self.frame)
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.horizontalLayout.addWidget(self.line_2)
        self.lbl_matches_found = QtWidgets.QLabel(self.frame)
        self.lbl_matches_found.setObjectName("lbl_matches_found")
        self.horizontalLayout.addWidget(self.lbl_matches_found)
        self.btn_prev_match = QtWidgets.QToolButton(self.frame)
        self.btn_prev_match.setObjectName("btn_prev_match")
        self.horizontalLayout.addWidget(self.btn_prev_match)
        self.btn_next_match = QtWidgets.QToolButton(self.frame)
        self.btn_next_match.setObjectName("btn_next_match")
        self.horizontalLayout.addWidget(self.btn_next_match)
        self.verticalLayout.addWidget(self.frame)
        self.txt_document = QtWidgets.QPlainTextEdit(RegexMatcherWidget)
        self.txt_document.setObjectName("txt_document")
        self.verticalLayout.addWidget(self.txt_document)

        self.retranslateUi(RegexMatcherWidget)
        QtCore.QMetaObject.connectSlotsByName(RegexMatcherWidget)

    def retranslateUi(self, RegexMatcherWidget):
        _translate = QtCore.QCoreApplication.translate
        RegexMatcherWidget.setWindowTitle(_translate("RegexMatcherWidget", "Regex Matcher"))
        self.btn_load_file.setText(_translate("RegexMatcherWidget", "Load from File"))
        self.btn_match_regex.setText(_translate("RegexMatcherWidget", "Find"))
        self.lbl_matches_found.setText(_translate("RegexMatcherWidget", "0 match(es) found"))
        self.btn_prev_match.setText(_translate("RegexMatcherWidget", "<"))
        self.btn_next_match.setText(_translate("RegexMatcherWidget", ">"))
        self.txt_document.setPlaceholderText(_translate("RegexMatcherWidget", "☝️ ... or directly paste from clipboard here"))
