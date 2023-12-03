from icecream import ic


def find_digit():
    with open('input.txt') as f:
        lines = f.read().splitlines()

        digits = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
        numbers_together = []

        for line in lines:  # line:str, lines: lst[line:str]
            local_number_digits = []
            for el in line:  # el: str
                if el in digits:  # el: str, digits:lst[str]
                    local_number_digits.append(el)
            numbers_together.append(local_number_digits)

    return numbers_together


def sum_digit(numbers_together):
    total_elements = []
    for element in numbers_together:
        total_elements.append(int(element[0] + element[-1]))
    return total_elements




if __name__ == '__main__':
    numbers_together = find_digit()
    ic(numbers_together)
    numbers = sum_digit(numbers_together)
    ic(numbers)
    ic(sum(numbers))

