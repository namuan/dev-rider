import re

from app.tools.tool_plugin import ToolPlugin
from app.views.regex_widget import RegexMatcherWidget


class RegexMatcher(ToolPlugin):
    def __init__(self):
        super().__init__(
            name="Regex Matcher", widget_class=RegexMatcherWidget
        )
        self.matches_found = []
        self.current_match = 0

    def bind_events(self):
        # bind ui events
        self.view.btn_load_file.pressed.connect(self.on_file_load)
        self.view.btn_match_regex.pressed.connect(self.on_match_regex)
        self.view.btn_prev_match.pressed.connect(self.on_prev_match)
        self.view.btn_next_match.pressed.connect(self.on_next_match)

    def on_file_load(self):
        file_contents = self.view.open_file()
        if file_contents:
            self.view.txt_document.setPlainText(file_contents)

    def on_match_regex(self):
        rgx = self.view.txt_regex.text()
        source = self.view.txt_document.toPlainText()
        if rgx and source:
            self.view.reset_highlights()
            self.matches_found = []

            compiled_rgx = re.compile(rgx)
            for m in compiled_rgx.finditer(source):
                start, end = m.span()
                self.view.highlight_match(start, end)
                self.matches_found.append(m)

            self.view.lbl_matches_found.setText("{} match(es) found".format(len(self.matches_found)))

    def goto_selected_match(self):
        match = self.matches_found[self.current_match]
        self.view.scroll_to_match(*match.span())

    def on_prev_match(self):
        if self.current_match > 0:
            self.current_match = self.current_match - 1

        self.goto_selected_match()

    def on_next_match(self):
        if self.current_match < len(self.matches_found) - 1:
            self.current_match = self.current_match + 1

        self.goto_selected_match()


tool = RegexMatcher()
