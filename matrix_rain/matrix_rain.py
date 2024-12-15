import os
import random
import re
import time
from typing import List
import iridis
from wcwidth import wcswidth

GREEN_SHADES = [
    "\033[2;32m",  # Dark Green
    "\033[32m",    # Normal Green
    "\033[1;32m",  # Bright Green
]
def remove_color_codes(text):
    return re.sub(r'\033\[[0-9;]*[mK]', '', text)

def truncate_to_width(text, width):
    clean_text = remove_color_codes(text)
    
    if wcswidth(clean_text) > width:
        truncated_text = ""
        for char in text:
            if wcswidth(remove_color_codes(truncated_text + char)) <= width:
                truncated_text += char
            else:
                break
        return truncated_text
    return text

def run_matrix_rain(symbols: List[str]) -> None:
    line_patterns_symbols = [" ", "$"]
    line_pattern = []

    console_width = os.get_terminal_size().columns
    console_length = os.get_terminal_size().lines

    for _ in range(console_width):
        symbol = random.choice(line_patterns_symbols)
        line_pattern.append(symbol)
        
    while True:
        os.system("clear" if os.name == "posix" else "cls")

        for _ in range(console_length - 1):
            line = ""
            for i, line_pattern_char in enumerate(line_pattern):
                if line_pattern_char == "$":
                    symbol = random.choice(symbols)

                    if random.choice(range(console_length // 7)) == 1:
                        symbol = " "
                        line_pattern[i] = " "

                    line += GREEN_SHADES[i % len(GREEN_SHADES)]
                    line += symbol
                    line += iridis.Color.RESET.value

                elif line_pattern_char == " ":
                    line += " "

                    if random.choice(range(int(console_length // 0.7))) == 1:
                        line_pattern[i] = "$" 

            print(truncate_to_width(line, console_width))
            time.sleep(0.1)
