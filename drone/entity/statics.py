from drone.entity.static import Static
from drone.entity.mobile import Mobile
from drone.sigil import Sigil


class Item(Static):
    def __init__(self, name: str, size: int,
                 sigil: Sigil = Sigil(char="◙",
                                      color=(220, 220, 220),
                                      bg_color=(0, 0, 0))):
        assert 0 <= size <= 10
        super().__init__(sigil, size, name)


class Stone(Item):
    def __init__(self):
        super().__init__(name="Rough Stone",
                         size=1)


class IronOre(Item):
    def __init__(self):
        super().__init__(name="Iron Ore",
                         size=2,
                         sigil=Sigil(char="•",
                                     color=(77, 166, 255),
                                     bg_color=(0, 0, 0)))

class Diggable(Static):
    def __init__(self,
                 hardness: float = 1,
                 mass: float = 1,
                 sigil=Sigil(char="█",
                             color=(220, 220, 220),
                             bg_color=(0, 0, 0))):

        super().__init__(sigil=sigil, size=10)
        self.hardness = hardness
        self.mass = mass
        self.mass_removed = 0

    def on_partially_dug(self, digger: Mobile):
        if self.mass_removed >= .75 * self.mass:
            self.sigil = Sigil(char="░",
                               color=self.sigil.color,
                               bg_color=self.sigil.bg_color)
        elif self.mass_removed >= .50 * self.mass:
            self.sigil = Sigil(char="▒",
                               color=self.sigil.color,
                               bg_color=self.sigil.bg_color)
        elif self.mass_removed >= .25 * self.mass:
            self.sigil = Sigil(char="▓",
                               color=self.sigil.color,
                               bg_color=self.sigil.bg_color)

    def on_fully_dug(self, digger: Mobile):
        """Override to, at the very least, drop something."""
        pass

    def dig(self, effort: float, digger: Mobile):
        removed = effort/self.hardness
        self.mass_removed = max(self.mass, self.mass_removed + removed)

        if self.mass_removed == self.mass:
            self.on_fully_dug(digger)
        else:
            self.on_partially_dug(digger)


class StoneTile(Diggable):
    def __init__(self):
        super().__init__(hardness=1,
                         mass=1)

    def on_fully_dug(self, digger: Mobile):
        reward = Stone()
        self.parent_cell.contents.remove(self)
        reward.introduce_at(self.parent_cell)


class IronOreTile(Diggable):
    def __init__(self):
        super().__init__(hardness=1.25,
                         mass=1.5,
                         sigil=Sigil(char="█",
                                     color=(77, 166, 255),
                                     bg_color=(0, 0, 0)))

    def on_fully_dug(self, digger: Mobile):
        # Clear self from the contents of its own cell and replace it with dropped iron ore
        reward = IronOre()
        self.parent_cell.contents.remove(self)
        reward.introduce_at(self.parent_cell)