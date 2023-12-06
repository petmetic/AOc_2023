from icecream import ic
import math


def parse_input():
    # lines = open("test_input.txt").read().splitlines()
    lines = open("input.txt").read().splitlines()

    time, ms = lines[0].split(':')
    tms = list(map(int, ms.split()))

    rec, rec_mm = lines[1].split(':')
    rec_mm = list(map(int, rec_mm.split()))

    return tms, rec_mm


def calc_dist(time):
    ms = []
    for sec in range(1, time):
        ms.append(sec)

    distances = []
    for hold in ms:
        dist = hold *(time - hold)
        distances.append(dist)
    return distances


def beat_rec_dist(tms, rec_mm):
    all_wins = []

    for idx, time in enumerate(tms):
        wins = 0
        distances = calc_dist(time)

        for dist in distances:
            if dist > rec_mm[idx]:
                wins += 1

        all_wins.append(wins)
    return all_wins


if __name__ == '__main__':
    tms, rec_mm = parse_input()
    ic(math.prod(beat_rec_dist(tms, rec_mm)))
