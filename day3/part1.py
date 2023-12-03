from icecream import ic


def find_digit():
    lines = open("test_input.txt").read().splitlines()
    # lines = open("input.txt").read().splitlines()

    simbols = []
    for line in lines: # find all simbols and their idx values
        for char in line:
            if char != '.':

                if  not char.isdigit():
                    simbols.append(char)





if __name__ == '__main__':
    numbers_together = find_digit()
