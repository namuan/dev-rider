# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'resources/views/MarkdownViewerWidget.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MarkdownViewerWidget(object):
    def setupUi(self, MarkdownViewerWidget):
        MarkdownViewerWidget.setObjectName("MarkdownViewerWidget")
        MarkdownViewerWidget.resize(713, 409)
        self.horizontalLayout = QtWidgets.QHBoxLayout(MarkdownViewerWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.txt_source = QtWidgets.QPlainTextEdit(MarkdownViewerWidget)
        self.txt_source.setObjectName("txt_source")
        self.horizontalLayout.addWidget(self.txt_source)
        self.frame = QtWidgets.QFrame(MarkdownViewerWidget)
        self.frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setLineWidth(0)
        self.frame.setObjectName("frame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.btn_raw_html = QtWidgets.QPushButton(self.frame)
        self.btn_raw_html.setObjectName("btn_raw_html")
        self.verticalLayout.addWidget(self.btn_raw_html)
        self.btn_render_html = QtWidgets.QPushButton(self.frame)
        self.btn_render_html.setObjectName("btn_render_html")
        self.verticalLayout.addWidget(self.btn_render_html)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.horizontalLayout.addWidget(self.frame)
        self.txt_target = QtWidgets.QTextEdit(MarkdownViewerWidget)
        self.txt_target.setReadOnly(True)
        self.txt_target.setObjectName("txt_target")
        self.horizontalLayout.addWidget(self.txt_target)

        self.retranslateUi(MarkdownViewerWidget)
        QtCore.QMetaObject.connectSlotsByName(MarkdownViewerWidget)

    def retranslateUi(self, MarkdownViewerWidget):
        _translate = QtCore.QCoreApplication.translate
        MarkdownViewerWidget.setWindowTitle(_translate("MarkdownViewerWidget", "Form"))
        self.txt_source.setPlainText(_translate("MarkdownViewerWidget", "### Heading\n"
"\n"
"Hello DevRider. This project is amazing...\n"
"\n"
"[Github Project](https://github.com/namuan/dev-rider)"))
        self.btn_raw_html.setText(_translate("MarkdownViewerWidget", "View Raw Html"))
        self.btn_render_html.setText(_translate("MarkdownViewerWidget", "Render Html"))
