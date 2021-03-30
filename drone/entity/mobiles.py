import numpy as np
import random as rand
from drone.entity import Mobile
from drone.sigil import Sigil


class Actor(Mobile):
    def act(self):
        pass

    def tick(self):
        if self.cooldown == 0:
            self.act()
        self.cooldown -= 1


class DemoBoi(Actor):
    def __init__(self):
        super().__init__(name="Demo Boi",
                         size=4,
                         sigil=Sigil(char="@",
                                     color=(190, 190, 250),
                                     bg_color=(0, 0, 0)),
                         base_action_cost=10)

    def act(self):
        # DemoBoi just wants to wander to a random passable neighbor
        x, y = self.parent_cell.x, self.parent_cell.y
        height, width = self.parent_cell.parent.height, self.parent_cell.parent.width
        neighbors = sum([[(x + dx, y + dy)
                          for dx in (-1, 0, 1)
                          if 0 <= x + dx < width and 0 <= y + dy < height]
                         for dy in (-1, 0, 1)],
                        [])

        neighbor_cells = [self.parent_cell.parent.cell_at(x_, y_) for x_, y_ in neighbors]
        passable_neighbors = [c for c in neighbor_cells if c.can_accept(self)]

        destination = rand.choice(passable_neighbors)

        self.move_to(destination.x, destination.y)
        self.cooldown = self.base_action_cost
