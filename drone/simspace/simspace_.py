import numpy as np

from typing import List, Tuple, Dict
from drone.simspace.cell import Cell


class SimSpace:
    def __init__(self, width: int, height: int):
        # self.cells: List[Cell] = sum([[Cell(x, y, self)
        #                                for x in range(0, width)]
        #                               for y in range(0, height)],
        #                              [])
        self.cells: Dict = {}

        self.width = width
        self.height = height

    def cell_at(self, x, y):
        # Is there a more efficient way to do this?
        return [c for c in self.cells if c.x == x and x.y == y][0]