import numpy as np
import random as rand

from drone.entity.statics import StoneTile


class TipsyWalker:
    def __init__(self, x0, y0, x1, y1, field: np.ndarray):
        self.start = x0, y0
        self.here = x0, y0
        self.end = x1, y1
        self.field = field

    def paint(self, x, y):
        self.field[y, x] = True

    def tick(self, stagger_prob):
        # First, we paint from where we are.
        self.paint(self.here[0], self.here[1])

        # Clockwise from up
        deltas = [(0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1)]
        dx, dy = (self.end[0] - self.here[0],
                  self.end[1] - self.here[1])

        # Smoosh deltas to target to -1, 0, 1 based on their signs
        dx = max(dx, -1) if dx < 0 else min(dx, 1)
        dy = max(dy, -1) if dy < 0 else min(dy, 1)

        # Decide on an orthogonal direction in which to move
        can_go_dx = dx != 0
        can_go_dy = dy != 0

        # If we can move either direction, choose randomly. Otherwise choose as appropriate.
        if can_go_dx and can_go_dy:
            best_direction = (dx, 0) if rand.random() <= 0.5 else (0, dy)
        elif can_go_dy:
            best_direction = (0, dy)
        elif can_go_dx:
            best_direction = (dx, 0)
        else:
            best_direction = (0, 0)

        # Decide whether to stagger
        if best_direction == (0, 0):
            direction = best_direction
        elif stagger_prob <= rand.random():
            # Choose clockwise or counterclockwise
            dir_index = deltas.index(best_direction)
            offset = 1 if rand.random() <= 0.5 else -1

            direction = deltas[(dir_index + offset) % len(deltas)]
        else:
            direction = best_direction

        destination = (self.here[0] + direction[0],
                       self.here[1] + direction[1])

        # Move to that destination, if it's valid.
        height, width = self.field.shape
        if 0 <= destination[0] < width and 0 <= destination[1] < height:
            self.here = (self.here[0] + direction[0],
                         self.here[1] + direction[1])


def rockface(width, height, stagger_prob=0.35,
             start_y=12,
             end_y=11):
    field: np.ndarray = np.full(shape=(height, width),
                                fill_value=False)

    start = 0, start_y
    end = width-1, end_y
    artist = TipsyWalker(x0=start[0], y0=start[1],
                         x1=end[0], y1=end[1],
                         field=field)

    artist.tick(stagger_prob=stagger_prob)

    # Iterate until the artist reaches the destination or gets stuck n times.
    last_tile = artist.here
    same_tile_limit = 5000
    same_tile_count = 0
    while artist.here != end and same_tile_count < same_tile_limit:
        artist.tick(stagger_prob=stagger_prob)
        if artist.here == last_tile:
            same_tile_count += 1

    # Draw from the bottom up
    # Start by gathering the first True cell in each column
    columns = [c for c in field.transpose()]

    #last_true_cells = [[el for el in c][-1:].index(True) for c in columns]
    last_true_cells = [[el for el in col].index(True) for col in columns]

    # For each of those columns, backfill from the artist's line to the first map edge
    for x, last_true_y in enumerate(last_true_cells):
        for y in range(last_true_y, height):
            field[y, x] = True

    # Cast to a dict of position keys and cell contents
    contents = {}
    for pos, truth in np.ndenumerate(field):
        if truth:
            y, x = pos
            contents[(x, y)] = [StoneTile()]

    return contents
