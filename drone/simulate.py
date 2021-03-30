"""Runs the loop and manages the stack of interfaces."""

import tcod
import multiprocessing as mp

from time import time_ns
from drone.interface import SimInterface
from drone.simspace import SimSpace
from drone.simfield_generator.rockface_gen import rockface

FLAGS = tcod.context.SDL_WINDOW_FULLSCREEN_DESKTOP
WIDTH, HEIGHT = 76, 54


def __time_ms():
    """We're gonna clock the game in milliseconds, so using 1e6 * epoch nanoseconds should be fine."""
    return int(time_ns()/1000000)


def main():
    mp.freeze_support()

    tileset = tcod.tileset.load_tilesheet("tilesets/yayo_c64_16x16.png", 16, 16,
                                          charmap=tcod.tileset.CHARMAP_CP437)
    context = tcod.context.new(width=WIDTH,
                               height=HEIGHT,
                               tileset=tileset,
                               sdl_window_flags=FLAGS)

    # Spin up the interfaces list, including the base simulation interface
    interfaces = []
    SimInterface(80, 60, interfaces,
                 simspace=SimSpace(width=80, height=60))

    # Render a rockface for demo purposes
    for position, contents in rockface(width=80, height=60,
                                       stagger_prob=0.05).items():
        x, y = position
        for ent in contents:
            space: SimSpace = interfaces[0].simspace
            ent.introduce_at(space.cell_at(x, y))

    from drone.entity.mobiles import DemoBoi
    boi = DemoBoi()
    space = interfaces[0].simspace
    boi.introduce_at(space.cell_at(20, 0))
    #print(space.cell_at(20, 0).contents)

    # Clock and execute the main loop
    last_tick = __time_ms()  # In epoch milliseconds
    tick_length = 5          # Milliseconds per engine tick
    while True:
        now_ms = __time_ms()
        # Only run the main loop logic if we've reached the next clock increment
        if now_ms - last_tick >= tick_length:
            # Grab a fresh console
            console = context.new_console(min_rows=60,
                                          min_columns=80)

            # Print Interfaces
            for i in interfaces:
                i.tick()
                i.print_to_console(console=console)

            # Render the new console
            context.present(console)

            # Pass out events
            last_handler = interfaces[-1].handler
            for event in tcod.event.get():
                last_handler.dispatch(event)

            last_tick = now_ms


if __name__ == "__main__":
    main()
