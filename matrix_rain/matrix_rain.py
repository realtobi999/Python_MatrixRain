import io
import sys
import random
import time
import numpy as np
import keyboard
import os
from iridis import Color
from typing import List

TERMINAL_WIDTH, TERMINAL_HEIGHT = os.get_terminal_size()
COLORS = {
    "green": [Color.GREEN.value, Color.BOLD_GREEN.value, Color.HIGH_INT_GREEN.value, Color.BOLD_HIGH_INT_GREEN.value],
    "red": [Color.RED.value, Color.BOLD_RED.value, Color.HIGH_INT_RED.value, Color.BOLD_HIGH_INT_RED.value],
    "blue": [Color.BLUE.value, Color.BOLD_BLUE.value, Color.HIGH_INT_BLUE.value, Color.BOLD_HIGH_INT_BLUE.value],
    "yellow": [Color.YELLOW.value, Color.BOLD_YELLOW.value, Color.HIGH_INT_YELLOW.value, Color.BOLD_HIGH_INT_YELLOW.value],
    "purple": [Color.PURPLE.value, Color.BOLD_PURPLE.value, Color.HIGH_INT_PURPLE.value, Color.BOLD_HIGH_INT_PURPLE.value],
    "cyan": [Color.CYAN.value, Color.BOLD_CYAN.value, Color.HIGH_INT_CYAN.value, Color.BOLD_HIGH_INT_CYAN.value],
}


def update_screen_dimensions() -> bool:
    global TERMINAL_WIDTH, TERMINAL_HEIGHT
    current_width, current_height = os.get_terminal_size()
    if (TERMINAL_WIDTH, TERMINAL_HEIGHT) != (current_width, current_height):
        TERMINAL_WIDTH, TERMINAL_HEIGHT = current_width, current_height
        return True
    return False


def start_rainfall(symbols: List[str]) -> None:
    # Initialize the screen as a 2D NumPy array filled with zeros.
    screen = np.zeros((TERMINAL_HEIGHT, TERMINAL_WIDTH), dtype=np.int8)
    default_colors_scheme = COLORS["green"]

    while True:
        # Handle keyboard input.
        if keyboard.is_pressed("q"):
            break
        if keyboard.is_pressed("c"):
            time.sleep(1)

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
        screen[1:] = screen[:-1]
        screen[0, :] = 0

        # Buffer for screen output
        screen_buffer = io.StringIO()

        # Build the screen output in memory before writing to stdout
        rows = []
        for row in range(TERMINAL_HEIGHT):
            row_chars = []
            for col in range(TERMINAL_WIDTH):
                if screen[row][col] == 1:
                    symbol = random.choice(symbols)
                    color = random.choice(default_colors_scheme)
                    row_chars.append(f"{color}{symbol}{Color.RESET.value}")
                else:
                    row_chars.append(" ")
            rows.append("".join(row_chars))

        # Write the entire screen to the buffer
        screen_buffer.write("\n".join(rows))

        sys.stdout.write("\033[H\033[J")
        sys.stdout.write(screen_buffer.getvalue())

        sys.stdout.flush()
        screen_buffer.close()

        time.sleep(0.025)
