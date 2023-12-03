from icecream import ic
import re


def find_all(needle, haystack):
    return [m.start() for m in re.finditer(needle, haystack)]


def find_symbols():
    lines = open("test_input.txt").read().splitlines()
    # lines = open("input.txt").read().splitlines()
    ic(lines)

    symbols = []
    digits = []
    for idx_line, line in enumerate(lines):  # find all simbols and their idx values
        for idx, char in enumerate(line):
            if char != '.':
                if char.isdigit():
                    digits.append([idx_line, idx, char])
                else:
                    symbols.append([idx_line, idx, char])
    return symbols, digits




def find_digits(symbols):
    ic(symbols)
    for symbol in symbols:
        y_coordinate, x_coordinate, symbol = symbol
        ic(symbol)
        ic(y_coordinate)
        ic(x_coordinate)



if __name__ == '__main__':
    symbols, digits = find_symbols()
    digits = find_digits(symbols)
    # ic(numbers)
