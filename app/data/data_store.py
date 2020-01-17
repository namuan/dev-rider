import logging

import dataset

from app.data.entities import AppState, APP_STATE_RECORD_TYPE
from app.events.signals import AppSignals


class DataStore:
    signals = AppSignals()

    def __init__(self, data_dir):
        self.data_dir = data_dir
        db_path = f"sqlite:///{self.data_dir}/devrider.db"
        self.db = dataset.connect(db_path)
        self._app_state = self.get_app_state()

    @property
    def app_state(self):
        return self._app_state

    def update_app_state_in_db(self):
        table = self.db[self.app_state.record_type]
        table.upsert(
            dict(
                name=self.app_state.record_type,
                object=self.app_state.to_json_str()
            ),
            ['name']
        )

    def get_app_state(self):
        table = self.db[APP_STATE_RECORD_TYPE]
        app_state_db = table.find_one(name=APP_STATE_RECORD_TYPE)
        if not app_state_db:
            return AppState()

        return AppState.from_json_str(app_state_db["object"])

    def update_selected_tool(self, selected_tool):
        logging.debug("Updating selected tool to {}".format(selected_tool))
        self.app_state.selected_tool = selected_tool
        self.update_app_state_in_db()
        self.signals.tool_switched.emit(selected_tool)

    def get_selected_tool(self):
        return self.app_state.selected_tool
