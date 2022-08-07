"""case style converter"""

import re

import sublime
import sublime_plugin

from .api import converter


command_map = {
    "camel": converter.to_camel,
    "upper_camel": converter.to_upper_camel,
    "snake": converter.to_snake,
    "upper_snake": converter.to_upper_snake,
}


class CaseStyleConvertCommand(sublime_plugin.TextCommand):
    """CaseStyleConvertCommand"""

    def run(self, edit, style):
        for selection in self.view.sel():
            word = self.view.word(selection)
            text = self.view.substr(word)

            if command := command_map.get(style):
                new_text = command(text)

                # only replace if text changed
                if text != new_text:
                    self.view.replace(edit, word, new_text)
            else:
                print(f"invalid style {style}")
