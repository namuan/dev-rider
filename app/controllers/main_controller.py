import logging

from app.settings.app_settings import app


class MainWindowController:
    def __init__(self, parent_window):
        self.parent = parent_window
        self.initial_load = True
        app.init()
        app.init_logger()
        if app.geometry():
            self.parent.restoreGeometry(app.geometry())
        if app.window_state():
            self.parent.restoreState(app.window_state())

    def save_settings(self):
        logging.info("Saving settings for Main Window")
        app.save_window_state(
            geometry=self.parent.saveGeometry(),
            window_state=self.parent.saveState()
        )

    def shutdown(self):
        self.save_settings()

    def after_window_loaded(self):
        if not self.initial_load:
            return

        self.initial_load = False
        self.init()

    def init(self):
        self.parent.toolbar_controller.init()
