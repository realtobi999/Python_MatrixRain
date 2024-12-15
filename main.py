import os
import matrix_rain

if __name__ == "__main__":
    os.system("clear" if os.name == "posix" else "cls")

    symbols = ["0", "1"] # + list("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")
    
    matrix_rain.start_rainfall(symbols=symbols)