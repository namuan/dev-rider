from PyQt5 import QtWidgets

from app.generated.MarkdownViewerWidget_ui import Ui_MarkdownViewerWidget


class MarkdownViewerWidget(QtWidgets.QWidget, Ui_MarkdownViewerWidget):
    def __init__(self, parent=None):
        super(MarkdownViewerWidget, self).__init__(parent)
        self.setupUi(self)
