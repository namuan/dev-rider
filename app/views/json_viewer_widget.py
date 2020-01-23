from PyQt5 import QtWidgets

from app.generated.JsonViewerWidget_ui import Ui_JsonViewerWidget
from app.themes.theme_provider import pyg_styles


class JsonViewerWidget(QtWidgets.QWidget, Ui_JsonViewerWidget):
    def __init__(self, parent=None):
        super(JsonViewerWidget, self).__init__(parent)
        self.setupUi(self)
        self.txt_json.document().setDefaultStyleSheet(pyg_styles())
