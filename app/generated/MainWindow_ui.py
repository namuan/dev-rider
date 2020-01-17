# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'resources/views/MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(978, 723)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.splitter_2 = QtWidgets.QSplitter(self.centralwidget)
        self.splitter_2.setOrientation(QtCore.Qt.Vertical)
        self.splitter_2.setObjectName("splitter_2")
        self.topFrame = QtWidgets.QFrame(self.splitter_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.topFrame.sizePolicy().hasHeightForWidth())
        self.topFrame.setSizePolicy(sizePolicy)
        self.topFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.topFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.topFrame.setObjectName("topFrame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.topFrame)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.splitter = QtWidgets.QSplitter(self.topFrame)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.toolScrollArea = QtWidgets.QScrollArea(self.splitter)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.toolScrollArea.sizePolicy().hasHeightForWidth())
        self.toolScrollArea.setSizePolicy(sizePolicy)
        self.toolScrollArea.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.toolScrollArea.setWidgetResizable(True)
        self.toolScrollArea.setObjectName("toolScrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 665, 426))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.toolWidgetLayout = QtWidgets.QHBoxLayout(self.scrollAreaWidgetContents)
        self.toolWidgetLayout.setContentsMargins(0, 0, 0, 0)
        self.toolWidgetLayout.setObjectName("toolWidgetLayout")
        self.toolScrollArea.setWidget(self.scrollAreaWidgetContents)
        self.historyFrame = QtWidgets.QFrame(self.splitter)
        self.historyFrame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.historyFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.historyFrame.setObjectName("historyFrame")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.historyFrame)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.listWidget = QtWidgets.QListWidget(self.historyFrame)
        self.listWidget.setObjectName("listWidget")
        self.horizontalLayout_2.addWidget(self.listWidget)
        self.horizontalLayout.addWidget(self.splitter)
        self.codegenFrame = QtWidgets.QFrame(self.splitter_2)
        self.codegenFrame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.codegenFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.codegenFrame.setObjectName("codegenFrame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.codegenFrame)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame = QtWidgets.QFrame(self.codegenFrame)
        self.frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.cmb_languages = QtWidgets.QComboBox(self.frame)
        self.cmb_languages.setObjectName("cmb_languages")
        self.cmb_languages.addItem("")
        self.cmb_languages.addItem("")
        self.cmb_languages.addItem("")
        self.cmb_languages.addItem("")
        self.horizontalLayout_3.addWidget(self.cmb_languages)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.btn_copy_clipboard = QtWidgets.QPushButton(self.frame)
        self.btn_copy_clipboard.setObjectName("btn_copy_clipboard")
        self.horizontalLayout_3.addWidget(self.btn_copy_clipboard)
        self.verticalLayout.addWidget(self.frame)
        self.txt_code = QtWidgets.QPlainTextEdit(self.codegenFrame)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.txt_code.setFont(font)
        self.txt_code.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.txt_code.setReadOnly(True)
        self.txt_code.setObjectName("txt_code")
        self.verticalLayout.addWidget(self.txt_code)
        self.horizontalLayout_5.addWidget(self.splitter_2)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "DevRider :: Development Tools"))
        self.cmb_languages.setItemText(0, _translate("MainWindow", "Java"))
        self.cmb_languages.setItemText(1, _translate("MainWindow", "Javascript"))
        self.cmb_languages.setItemText(2, _translate("MainWindow", "Node.js"))
        self.cmb_languages.setItemText(3, _translate("MainWindow", "Python"))
        self.btn_copy_clipboard.setText(_translate("MainWindow", "Clipboard"))
