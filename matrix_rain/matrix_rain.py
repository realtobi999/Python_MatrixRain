import os
import random
import sys
import time
import keyboard
import numpy as np
from typing import List

TERMINAL_WIDTH, TERMINAL_HEIGHT = os.get_terminal_size()
COLORS = {
    "green": ["\033[32m", "\033[1;32m", "\033[2;32m"],
    "red": ["\033[31m", "\033[1;31m", "\033[2;31m"],
    "blue": ["\033[34m", "\033[1;34m", "\033[2;34m"],
}


def print_and_clear_screen(screen_str: str):
    sys.stdout.write("\033[2J\033[H")
    sys.stdout.write(screen_str)
    sys.stdout.flush()


def shift_column_down(column):
    column[1:] = column[:-1]
    column[0] = 0


def update_screen_dimensions() -> bool:
    global TERMINAL_WIDTH, TERMINAL_HEIGHT
    current_width, current_height = os.get_terminal_size()
    if (TERMINAL_WIDTH, TERMINAL_HEIGHT) != (current_width, current_height):
        TERMINAL_WIDTH, TERMINAL_HEIGHT = current_width, current_height
        return True
    return False


def start_rainfall(symbols: List[str]) -> None:
    # Initialize the screen as a 2D NumPy array filled  with  zeros.  The  array
    # represents the terminal screen, where each element (0 or 1) corresponds to
    # a position on the screen. A value of 0 means the position is empty, and  a
    # value of 1 means it's part of a falling rain column.
    screen = np.zeros((TERMINAL_HEIGHT, TERMINAL_WIDTH), dtype=np.int8)
    default_colors_scheme = COLORS["green"]

    while True:
        # Handle keyboard input.
        if keyboard.is_pressed("q"):
            return
        if keyboard.is_pressed("c"):
            # Iterate through the default colors pattern.
            color_keys = list(COLORS.values())
            current_index = color_keys.index(default_colors_scheme)
            next_index = (current_index + 1) % len(color_keys)
            default_colors_scheme = color_keys[next_index]

        # If the screen width and height were changed, create a new screen.
        if update_screen_dimensions():
            screen = np.zeros((TERMINAL_HEIGHT, TERMINAL_WIDTH), dtype=np.int8)

        # Randomly generate new raindrops.
        for col in range(TERMINAL_WIDTH):
            if random.random() < 0.01:
                drop_length = random.randint(5, 6)
                for i in range(min(drop_length, TERMINAL_HEIGHT)):
                    screen[i][col] = 1

        # Shift the whole screen down by one to create the 'falling' effect.
        for col in range(TERMINAL_WIDTH):
            shift_column_down(screen[:, col])

        # Print and adjust speed.
        time.sleep(0.1)

        output_rows = [
            "".join(f"{random.choice(default_colors_scheme)}{random.choice(symbols)}\033[0m" if cell == 1 else " " for cell in row) for row in screen
        ]
        print_and_clear_screen("\n".join(output_rows))
