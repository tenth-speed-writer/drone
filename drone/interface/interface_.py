import tcod
from typing import List, Dict, Tuple


class Interface:
    """Combines an event handler and some on-screen content.
    The main loop renders each in order and hands event control to the last."""

    def __init__(self, width: int, height: int,
                 handler: tcod.event.EventDispatch,
                 interfaces: List,
                 tick_when_not_top: bool = False):
        self.height = height
        self.width = width
        self.tick_when_not_top = tick_when_not_top

        # Tuples of (character, color, bg_color) keyed by (x, y)
        self.field: Dict = {}

        # handler is an event dispatcher subclass
        self.handler = handler

        # interfaces is the list of active interfaces
        self.interfaces = interfaces
        self.interfaces.append(self)

    def tick(self):
        """Override to tick subordinate elements of this interface."""
        pass

    def print_to_console(self,
                         console: tcod.console.Console):
        for pos, vals in self.field.items():
            x, y = pos
            char, fg, bg = vals
            console.print(x=x, y=y,
                          string=char,
                          fg=fg, bg=bg)