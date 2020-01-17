from typing import Dict


class ToolPlugin:
    _name: str = None
    _widget_class: str = None
    _code_generator: Dict = {}
    _view = None

    def __init__(self, name, widget_class, code_generator):
        self._name = name
        self._widget_class = widget_class
        self._code_generator = code_generator

    def init_view(self, view):
        self._view = view
        self.bind_events()

    def bind_events(self):
        raise NotImplementedError("Should be implemented by {}".format(self.__class__))

    def generate_code(self, language):
        return self._code_generator.get(language)()

    @property
    def languages(self):
        return self._code_generator.keys()

    @property
    def view(self):
        if self._view is None:
            raise NotImplementedError("view should be provided")
        return self._view

    @property
    def name(self):
        if self._name is None:
            raise NotImplementedError("name should be provided")
        return self._name

    @property
    def widget_class(self):
        if self._widget_class is None:
            raise NotImplementedError("widget_class should be provided")
        return self._widget_class
