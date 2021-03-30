import tcod


class Interface:
    """Combines an event handler and some on-screen content.
    The main loop renders each in order and hands event control to the last."""

    def __init__(self, handler: tcod.event.EventDispatch):
        pass