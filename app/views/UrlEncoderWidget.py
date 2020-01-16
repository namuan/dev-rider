from PyQt5 import QtWidgets

from app.generated.UrlEncoderWidget_ui import Ui_UrlEncoderWidget


class UrlEncoderWidget(QtWidgets.QWidget, Ui_UrlEncoderWidget):
    def __init__(self, parent=None):
        super(UrlEncoderWidget, self).__init__(parent)
        self.setupUi(self)
