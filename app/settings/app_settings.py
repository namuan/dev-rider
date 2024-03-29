import logging
import logging.handlers
from pathlib import Path
from typing import Any, Union

from PyQt5.QtCore import QSettings, QStandardPaths
from PyQt5.QtWidgets import qApp

from app.core.str_utils import str_to_bool
from app.data.data_store import DataStore
from app.settings.app_config import AppConfig


class AppSettings:
    def __init__(self):
        self.settings: QSettings = None
        self.app_name: str = None
        self.app_dir: Union[Path, Any] = None
        self.docs_location: Path = Path(
            QStandardPaths.writableLocation(QStandardPaths.DocumentsLocation)
        )
        self.data: DataStore = None

    def init(self):
        self.app_name = qApp.applicationName().lower()
        self.app_dir = Path(
            QStandardPaths.writableLocation(QStandardPaths.AppConfigLocation)
        )
        self.app_dir.mkdir(exist_ok=True)
        settings_file = f"{self.app_name}.ini"
        self.settings = QSettings(
            self.app_dir.joinpath(settings_file).as_posix(), QSettings.IniFormat
        )
        self.settings.sync()
        self.data = DataStore(self.app_dir)

    def init_logger(self):
        log_file = f"{self.app_name}.log"
        handlers = [
            logging.handlers.RotatingFileHandler(
                self.app_dir.joinpath(log_file), maxBytes=1000000, backupCount=1
            ),
            logging.StreamHandler(),
        ]

        logging.basicConfig(
            handlers=handlers,
            format="%(asctime)s - %(filename)s:%(lineno)d - %(message)s",
            datefmt="%Y-%m-%d %H:%M:%S",
            level=logging.DEBUG,
        )
        logging.captureWarnings(capture=True)

    def save_window_state(self, geometry, window_state):
        self.settings.setValue("geometry", geometry)
        self.settings.setValue("windowState", window_state)
        self.settings.sync()

    def save_configuration(self, app_config):
        self.settings.setValue(AppConfig.STARTUP_CHECK_KEY, app_config.startup_check)
        self.settings.sync()

    def load_configuration(self):
        app_config = AppConfig()
        settings_value = self.settings.value(
            AppConfig.STARTUP_CHECK_KEY, app_config.startup_check
        )
        app_config.startup_check = str_to_bool(settings_value)
        return app_config

    def geometry(self):
        return self.settings.value("geometry", None)

    def window_state(self):
        return self.settings.value("windowState", None)


app = AppSettings()
