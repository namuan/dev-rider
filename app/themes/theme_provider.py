import darkdetect
from PyQt5.QtGui import QFont, QIcon, QFontDatabase

from themes.theme_loader import ThemeLoader


def is_dark():
    return darkdetect.isDark()


def configure_theme(app):
    app.setWindowIcon(QIcon(':/icons/app.svg'))

    app.setStyle(ThemeLoader())
    theme_mode = "dark" if is_dark() else "light"
    app.style().load_stylesheet(theme_mode)

    font_db = QFontDatabase()
    font_db.addApplicationFont(':/fonts/JetBrainsMono-Regular.ttf')

    current_font: QFont = QFont('JetBrains Mono')
    current_font.setPointSize(14)
    app.setFont(current_font)
