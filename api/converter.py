"""case converver"""

import re
from typing import Iterator


class WordSplitter:
    """word splitter"""

    lower_word = re.compile(r"([a-z0-9]+)")
    camel_word = re.compile(r"([A-Z][a-z0-9]+)")
    snake_word = re.compile(r"_?([A-Z-a-z]+)")

    def __init__(self, text: str):
        self.text = text
        self.cursor = 0

    def next_word(self) -> str:
        """get next word"""
        text = self.text[self.cursor :]

        if match := self.lower_word.match(text):
            self.cursor += match.end()
            return match.group(1)

        if match := self.camel_word.match(text):
            self.cursor += match.end()
            return match.group(1)

        if match := self.snake_word.match(text):
            self.cursor += match.end()
            if self.cursor == 0:
                # include underscore for beginning word
                return text[: self.cursor]
            return match.group(1)

        self.cursor += len(text)
        return text

    def words(self) -> Iterator[str]:
        """all words"""

        self.cursor = 0
        end_cursor = len(self.text)

        while True:
            if word := self.next_word():
                yield word

            if self.cursor == end_cursor:
                break


def to_camel(text) -> str:
    ws = WordSplitter(text)
    prefix, *words = list(ws.words())
    words = [word.title() for word in words]
    return f"{prefix}{''.join(words)}"


def to_upper_camel(text) -> str:
    ws = WordSplitter(text)
    words = [word.title() for word in ws.words()]
    return "".join(words)


def to_snake(text) -> str:
    ws = WordSplitter(text)
    words = [word.lower() for word in ws.words()]
    return "_".join(words)


def to_upper_snake(text) -> str:
    ws = WordSplitter(text)
    words = [word.upper() for word in ws.words()]
    return "_".join(words)
