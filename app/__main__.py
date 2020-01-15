import sys

from PyQt5.QtGui import QFontDatabase, QFont, QIcon
from PyQt5.QtCore import QFile, QTextStream
from PyQt5.QtWidgets import QApplication

from app.views.MainWindow import MainWindow


def main():
    app = QApplication(sys.argv)

    app.setWindowIcon(QIcon(':/icons/app.svg'))

    f = QFile(':/style.qss')
    f.open(QFile.ReadOnly | QFile.Text)
    app.setStyleSheet(QTextStream(f).readAll())
    f.close()

    mw = MainWindow()
    mw.show()

    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
