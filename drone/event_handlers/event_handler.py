from tcod.event import EventDispatch


class EventHandler(EventDispatch):
    def ev_quit(self, event):
        raise SystemExit

    def ev_windowclose(self, event):
        raise SystemExit