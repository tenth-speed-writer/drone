import numpy as np

from typing import List, Tuple, Dict
from drone.simspace.cell import Cell


class SimSpace:
    def __init__(self, width: int, height: int):
        # Store cells as a dictionary keyed by (x, y) position tuples
        cell_positions = sum([[(x, y)
                               for y in range(0, height)]
                              for x in range(0, width)],
                             [])
        self.cells: Dict = {}
        for x, y in cell_positions:
            self.cells[(x, y)] = Cell(x, y, self)

        self.width = width
        self.height = height

    def cell_at(self, x, y):
        return self.cells[(x, y)]

    @property
    def entities(self):
        """Returns a flattened list of all entities in the simspace."""
        contents = [cell.contents for pos, cell in self.cells.items()]
        return sum(contents, [])

    def tick(self):
        """Tick every entity in the simspace."""
        [e.tick() for e in self.entities]