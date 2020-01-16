from typing import ClassVar

import attr


@attr.s(auto_attribs=True)
class AppConfig:
    STARTUP_CHECK_KEY: ClassVar[str] = "startupCheck"
    _startup_check: bool = True

    @property
    def startup_check(self):
        return self._startup_check

    @startup_check.setter
    def startup_check(self, val):
        self._startup_check = val
