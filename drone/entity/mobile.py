from drone.entity.entity_ import Entity


class Mobile(Entity):
    def move_to(self, x, y):
        at = self.parent_cell
        tgt = self.parent_cell.parent.cell_at(x, y)

        if tgt.can_accept(self):
            at.contents.remove(self)
            tgt.contents.append(self)

        else:
            print("Tried to move {} to {}, {}, but it couldn't be accepted."
                  .format(str(self), str(x), str(y)))