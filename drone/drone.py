"""Runs the loop and manages the stack of interfaces."""

import tcod
import multiprocessing as mp
from time import time_ns

FLAGS = tcod.context.SDL_WINDOW_FULLSCREEN_DESKTOP
WIDTH, HEIGHT = 76, 54


def __time_ms():
    """We're gonna clock the game in milliseconds, so using 1000 * epoch nanoseconds should be fine."""
    return int(time_ns()/1000000)


def main():
    mp.freeze_support()

    tileset = tcod.tileset.load_tilesheet("tilesets/yayo_c64_16x16.png", 16, 16,
                                          charmap=tcod.tileset.CHARMAP_CP437)
    context = tcod.context.new(width=WIDTH,
                               height=HEIGHT,
                               tileset=tileset,
                               sdl_window_flags=FLAGS)

    last_tick = __time_ms()  # In epoch milliseconds
    tick_length = 50  # Milliseconds per engine tick
    while True:
        now_ms = __time_ms()
        # Only run the main loop logic if we've reached the next clock increment
        if now_ms - last_tick >= tick_length:
            # GAME LOGIC GOES HERE
            last_tick = now_ms