from typing import Tuple
from drone.sigil import Sigil


class Cell:
    def __init__(self, x: int, y: int, simspace, max_size: int = 10):
        self.x, self.y = x, y
        self.max_size = max_size
        self.contents = []
        self.parent = simspace

    @property
    def fullness(self):
        return sum([ent.size for ent in self.contents])

    def can_accept(self, ent):
        return ent.size + self.fullness <= self.max_size

    @property
    def printables(self) -> Tuple[int, int, Sigil]:
        max_size = max([c.size for c in self.contents])
        biggest = [c for c in self.contents if c.size == max_size][0]
        return self.x, self.y, biggest
