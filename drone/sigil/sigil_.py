from typing import Tuple


class Sigil:
    def __init__(self, char: str,
                 color: Tuple[int, int, int],
                 bg_color: Tuple[int, int, int]):
        assert len(char) == 1
        self.char = char

        assert sum([0 <= i <= 255 for i in color]) == 3
        self.color = color

        assert sum([0 <= i <= 255 for i in bg_color]) == 3
        self.bg_color = bg_color
