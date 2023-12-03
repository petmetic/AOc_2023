from icecream import ic
import re


def find_all(needle, haystack):
    return [m.start() for m in re.finditer(needle, haystack)]


def convert_digit(word):
    txt_trans = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9}
    if word in txt_trans.keys():  # word: is key of word dict
        return str(txt_trans[word])


def find_digit():
    with open('input.txt') as f:
        lines = f.read().splitlines()
        numbers = []
        for line in lines:  # line:str, lines: lst[line:str]
            digits_txt = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
            numbers_together = {}
            for word in digits_txt:
                all = find_all(word, line)
                for idx in all:
                    numbers_together[idx] = convert_digit(word)

            for idx, char in enumerate(line):
                if char.isdigit():
                    numbers_together[idx] = char
            numbers.append(numbers_together)

    return numbers

def sum_digits(lst_numbers):
    lst_sum_digits = []
    for numbers in lst_numbers:
        lst_of_nums = numbers.keys()
        sorted_lst_of_nums = sorted(lst_of_nums)

        low_idx = sorted_lst_of_nums[0]
        high_idx = sorted_lst_of_nums[-1]
        low_number = numbers[low_idx]  # get value
        high_number = numbers[high_idx]  # get value

        lst_sum_digits.append(int(low_number + high_number))

    return lst_sum_digits


if __name__ == '__main__':
    numbers = find_digit()
    lst_sum_digits = sum_digits(numbers)
    end_result = sum(lst_sum_digits)
    ic(end_result)
