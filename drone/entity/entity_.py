from typing import List, Tuple, Dict
from drone.sigil import Sigil


class Entity:
    parent_cell = None

    def __init__(self, sigil: Sigil, size: int, name: str = ""):
        self.sigil = sigil
        self.size = size
        self.name = name

    def introduce_at(self, cell):
        if cell.can_accept(self):
            self.parent_cell = cell
            cell.contents.append(self)
        else:
            print("Tried to place entity {} into cell {} at position {}, {}, but it had not enough room."
                  .format(str(self),
                          str(cell),
                          str(cell.x),
                          str(cell.y)))

    def tick(self):
        """Overridable. Logic to occur every simulation tick."""
        pass
