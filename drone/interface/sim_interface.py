import tcod

from typing import List
from drone.interface.interface_ import Interface
from drone.event_handlers.sim_handler import SimHandler
from drone.simspace.simspace_ import SimSpace


class SimInterface(Interface):
    def __init__(self, width: int, height: int,
                 interfaces: List[Interface],
                 simspace: SimSpace):
        super().__init__(width=width,
                         height=height,
                         handler=SimHandler(self),
                         interfaces=interfaces)

        # Generate a simspace if not issued one
        if simspace:
            assert simspace.width == self.width and simspace.height == self.height
            self.simspace = simspace
        else:
            self.simspace = SimSpace(width=width,
                                     height=height)

    def tick(self):
        # Tick the sim
        self.simspace.tick()

        # TODO: Sensible handling of multiple entities in one cell
        # Update the printable field
        field = {}
        for ent in self.simspace.entities:
            x, y = ent.parent_cell.x, ent.parent_cell.y
            char = ent.sigil.char
            fg = ent.sigil.color
            bg = ent.sigil.bg_color
            if not (x, y) in field.keys():
                field[(x, y)] = (char, fg, bg)
        self.field = field

    def print_to_console(self, console: tcod.console.Console):
        super().print_to_console(console)
