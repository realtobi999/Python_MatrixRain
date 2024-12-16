import os
import matrix_rain

if __name__ == "__main__":
    os.system("clear" if os.name == "posix" else "cls")

    symbols = ["0", "1"]  # + list("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")

    matrix_rain.start_rainfall(
        symbols=symbols,
        colors=[
            "\033[2;32m",  # Dark Green
            "\033[32m",  # Normal Green
            "\033[1;32m",  # Bright Green
        ],
    )
