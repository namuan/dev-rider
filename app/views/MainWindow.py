import logging
import sys
import traceback

from PyQt5.QtGui import QCloseEvent
from PyQt5.QtWidgets import QMainWindow, QToolBar, qApp

from app.controllers import *
from app.generated.MainWindow_ui import Ui_MainWindow
from app.widgets.shortcuts import shortcut_items
from app.widgets.toolbar import toolbar_items


class MainWindow(QMainWindow, Ui_MainWindow):
    """Main Window."""

    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)

        # Add components on Main Window
        self.toolbar = QToolBar()

        # Initialise controllers
        self.main_controller = MainWindowController(self)
        self.toolbar_controller = ToolbarController(self, self.toolbar)

        # Initialise components
        toolbar_items(self)
        shortcut_items(self)

        # Initialise Sub-Systems
        sys.excepthook = MainWindow.log_uncaught_exceptions

    # Main Window events
    def resizeEvent(self, event):
        self.main_controller.after_window_loaded()

    @staticmethod
    def log_uncaught_exceptions(cls, exc, tb) -> None:
        logging.critical(''.join(traceback.format_tb(tb)))
        logging.critical('{0}: {1}'.format(cls, exc))

    def closeEvent(self, event: QCloseEvent):
        logging.info("Received close event")
        event.accept()
        self.main_controller.shutdown()
        try:
            qApp.exit(0)
        except:
            pass

    def replace_widget(self, selected_widget):
        self.clear_layout(self.toolWidgetLayout)
        self.toolWidgetLayout.addWidget(selected_widget)

    def clear_layout(self, layout):
        for i in reversed(range(layout.count())):
            widget_item = layout.takeAt(i)
            if widget_item:
                widget_item.widget().deleteLater()
