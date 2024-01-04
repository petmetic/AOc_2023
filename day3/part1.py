from icecream import ic
import re


def find_all(needle, haystack):
    return [m.start() for m in re.finditer(needle, haystack)]


def find_symbols():
    # lines = open("test_input.txt").read().splitlines()
    lines = open("input.txt").read().splitlines()

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


def find_numbers(digits):
    nums = []
    x = None
    y = None
    c = ''

    for idx in range(0, len(digits)):
        ty, tx, tc = digits[idx]
        if idx + 1 == len(digits):
            c += tc
            nums.append([y, x, tx, c])
            break

        ny, nx, nc = digits[idx + 1]
        if not y:
            y = ty
        if x is None:
            x = tx
        if ty == ny:
            c += tc
            if nx != tx + 1:
                nums.append([y, x, tx, c])
                c = ''
                x = None
                y = None
        else:
            c += tc
            nums.append([y, x, tx, c])
            c = ''
            x = None
            y = None

    return nums


def compare_symbol_numbers(symbols, numbers):
    numbers_w_symbols = []
    for symbol in symbols:
        y, x, sim = symbol
        for number in numbers:
            ny, xs, xe, c = number

            transf = [(-1, 0), (0, -1), (1, 0), (0, 1), (-1, -1), (1, -1), (-1, 1), (1, 1)]
            for corner in transf:
                dy, dx = corner
                ty = y + dy  # transformed y from symbol
                tx = x + dx  # transformed x from symbol
                if tx in range(xs, xe + 1) and ty == ny:
                    numbers_w_symbols.append(int(c))
                    break

    return numbers_w_symbols


if __name__ == '__main__':
    symbols, digits = find_symbols()
    numbers = find_numbers(digits)
    connecting_numbers = (compare_symbol_numbers(symbols, numbers))
    result = sum(connecting_numbers)
    ic(result)
