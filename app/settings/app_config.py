class AppConfig:
    STARTUP_CHECK = False

    def __init__(self):
        self._startup_check = self.STARTUP_CHECK

    @property
    def startup_check(self):
        return self._startup_check

    @startup_check.setter
    def startup_check(self, val):
        self._startup_check = val
