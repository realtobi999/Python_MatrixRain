import os
from matrix_rain.matrix_rain import run_matrix_rain


if __name__ == "__main__":
    os.system("clear" if os.name == "posix" else "cls")

    symbols = ["0", "1"] # + list("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")
    
    run_matrix_rain(symbols=symbols)