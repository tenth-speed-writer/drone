from drone.event_handlers.event_handler import EventHandler


class SimHandler(EventHandler):
    def __init__(self, interface):
        self.interface = interface
