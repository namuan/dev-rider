# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'resources/views/JsonViewerWidget.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_JsonViewerWidget(object):
    def setupUi(self, JsonViewerWidget):
        JsonViewerWidget.setObjectName("JsonViewerWidget")
        JsonViewerWidget.resize(595, 492)
        self.verticalLayout = QtWidgets.QVBoxLayout(JsonViewerWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame = QtWidgets.QFrame(JsonViewerWidget)
        self.frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setLineWidth(0)
        self.frame.setObjectName("frame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btn_format_json = QtWidgets.QPushButton(self.frame)
        self.btn_format_json.setObjectName("btn_format_json")
        self.horizontalLayout.addWidget(self.btn_format_json)
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.val_indent_level = QtWidgets.QSpinBox(self.frame)
        self.val_indent_level.setProperty("value", 4)
        self.val_indent_level.setObjectName("val_indent_level")
        self.horizontalLayout.addWidget(self.val_indent_level)
        self.chk_sort_keys = QtWidgets.QCheckBox(self.frame)
        self.chk_sort_keys.setObjectName("chk_sort_keys")
        self.horizontalLayout.addWidget(self.chk_sort_keys)
        self.line = QtWidgets.QFrame(self.frame)
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.horizontalLayout.addWidget(self.line)
        self.btn_minify_json = QtWidgets.QPushButton(self.frame)
        self.btn_minify_json.setObjectName("btn_minify_json")
        self.horizontalLayout.addWidget(self.btn_minify_json)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.lbl_json_valid = QtWidgets.QLabel(self.frame)
        self.lbl_json_valid.setObjectName("lbl_json_valid")
        self.horizontalLayout.addWidget(self.lbl_json_valid)
        self.verticalLayout.addWidget(self.frame)
        self.txt_json = QtWidgets.QPlainTextEdit(JsonViewerWidget)
        self.txt_json.setPlainText("")
        self.txt_json.setObjectName("txt_json")
        self.verticalLayout.addWidget(self.txt_json)
        self.frame_2 = QtWidgets.QFrame(JsonViewerWidget)
        self.frame_2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setLineWidth(0)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout.addWidget(self.frame_2)

        self.retranslateUi(JsonViewerWidget)
        QtCore.QMetaObject.connectSlotsByName(JsonViewerWidget)

    def retranslateUi(self, JsonViewerWidget):
        _translate = QtCore.QCoreApplication.translate
        JsonViewerWidget.setWindowTitle(_translate("JsonViewerWidget", "Form"))
        self.btn_format_json.setText(_translate("JsonViewerWidget", "Format"))
        self.label.setText(_translate("JsonViewerWidget", "Indent"))
        self.chk_sort_keys.setText(_translate("JsonViewerWidget", "Sort Keys"))
        self.btn_minify_json.setText(_translate("JsonViewerWidget", "Minify"))
        self.lbl_json_valid.setText(_translate("JsonViewerWidget", "Valid"))
        self.txt_json.setPlaceholderText(_translate("JsonViewerWidget", "Paste JSON here ..."))
