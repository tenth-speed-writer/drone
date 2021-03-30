from drone.entity.entity_ import Entity


class Mobile(Entity):
    def __init__(self, sigil, size, name, base_action_cost):
        super().__init__(sigil, size, name)
        self.base_action_cost = base_action_cost
        self.cooldown = base_action_cost

    def move_to(self, x, y):
        #print("Contents :" + str(self.parent_cell.contents))
        at = self.parent_cell
        tgt = self.parent_cell.parent.cell_at(x, y)

        if tgt.can_accept(self):
            #print(at.contents)
            at.contents.remove(self)
            tgt.contents.append(self)
            self.parent_cell = tgt

        else:
            print("Tried to move {} to {}, {}, but it couldn't be accepted."
                  .format(str(self), str(x), str(y)))