import os
import random
import re
import time
import iridis
from typing import List
from wcwidth import wcswidth

TERMINAL_WIDTH, TERMINAL_HEIGHT = os.get_terminal_size()
COLOR_SHADES = [
    "\033[2;32m",  # Dark Green
    "\033[32m",  # Normal Green
    "\033[1;32m",  # Bright Green
]


def strip_ansi_color_codes(text):
    return re.sub(r"\033\[[0-9;]*[mK]", "", text)


def fit_to_width(text, max_width):
    clean_text = strip_ansi_color_codes(text)

    if wcswidth(clean_text) > max_width:
        clipped_text = ""
        for char in text:
            if wcswidth(strip_ansi_color_codes(clipped_text + char)) <= max_width:
                clipped_text += char
            else:
                break
        return clipped_text
    return text


def refresh_terminal_size() -> bool:
    resized = False

    global TERMINAL_WIDTH, TERMINAL_HEIGHT

    old_width, old_height = TERMINAL_WIDTH, TERMINAL_HEIGHT
    new_width, new_height = os.get_terminal_size()

    if old_width != new_width or old_height != new_height:
        os.system("clear" if os.name == "posix" else "cls")
        resized = True

    TERMINAL_WIDTH, TERMINAL_HEIGHT = new_width, new_height

    return resized


def start_rainfall(symbols: List[str]) -> None:
    columns_pattern_symbols = [" ", "$"]
    columns = []

    while True:
        row_index = 0
        while row_index in range(TERMINAL_HEIGHT - 1):
            resized = refresh_terminal_size()

            if len(columns) == 0 or resized:
                row_index = 0
                columns.extend([random.choice(columns_pattern_symbols)] * TERMINAL_WIDTH)

            row = ""
            for col_index, char in enumerate(columns):
                if char == "$":
                    symbol = random.choice(symbols)

                    if random.random() < 0.3:
                        columns[col_index] = " "
                        row += " "
                        continue

                    row += COLOR_SHADES[col_index % len(COLOR_SHADES)]
                    row += symbol
                    row += iridis.Color.RESET.value

                elif char == " ":
                    row += " "

                    if random.random() < 0.09:
                        columns[col_index] = "$"

            print(fit_to_width(row, TERMINAL_WIDTH))
            time.sleep(0.08)

            row_index += 1

        os.system("clear" if os.name == "posix" else "cls")
