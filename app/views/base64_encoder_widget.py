from PyQt5 import QtWidgets

from app.generated.Base64EncoderWidget_ui import Ui_Base64EncoderWidget


class Base64EncoderWidget(QtWidgets.QWidget, Ui_Base64EncoderWidget):
    def __init__(self, parent=None):
        super(Base64EncoderWidget, self).__init__(parent)
        self.setupUi(self)
