from PyQt5.QtCore import QObject, pyqtSignal


class AppSignals(QObject):
    tool_switched = pyqtSignal(str)


class AppCommands(QObject):
    pass
