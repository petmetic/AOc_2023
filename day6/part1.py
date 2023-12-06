from icecream import ic


def parse_input():
    lines = open("test_input.txt").read().splitlines()
    # lines = open("input.txt").read().splitlines()
    ic(lines)

    time, ms = lines[0].split(':')
    tms = list(map(int, ms.split()))

    rec, rec_mm = lines[1].split(':')
    rec_mm = list(map(int, rec_mm.split()))

    return tms, rec_mm


def calc_dist(time):
    ic(time)
    ms = []
    for sec in range(0, time + 1):
        ms.append(sec)

    ms.reverse()
    ic(ms)
    for sec in ms:
        hold = sec - 1
        time = sec - hold

        ic(hold, time, sec)

    # hold = time - 1
    # ic(hold)
    breakpoint()


def beat_rec_dist(tms, rec_mm):
    ic(tms, rec_mm)
    for time in tms:
        dist = calc_dist(time)


if __name__ == '__main__':
    tms, rec_mm = parse_input()
    beat_rec_dist(tms, rec_mm)
