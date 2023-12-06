from icecream import ic
import re


def parse_input():
    lines = open("test_input.txt").read().splitlines()
    # lines = open("input.txt").read().splitlines()

    # get seeds
    _, seeds = lines[0].split(': ')
    seeds = list(map(int, seeds.split()))

    return lines, seeds


def get_maps(lines, s_marker, e_marker):
    _map = []
    data = '\n'.join(lines[1::])
    pattern = rf'{s_marker}(.*?){e_marker}'
    match = re.search(pattern, data, re.DOTALL)

    if match:
        extracted_data = match.group(1).strip().split('\n')
        for el in extracted_data:
            seed_soil = {}
            el = el.strip(',')
            el = list(map(int, el.split()))
            d, s, l = el
            seed_soil["d"] = d
            seed_soil["s"] = s
            seed_soil["l"] = l
            _map.append(seed_soil)

    return _map


def get_stencil(seed, _map):
    for section in _map:
        d = section["d"]
        s = section["s"]
        l = section["l"]

        rl = range(s, s + l)

        if seed in rl:
            seed = seed - s + d
            return seed
    return seed


def next_map(seeds, _map):
    trans = []
    for seed in seeds:
        seed = get_stencil(seed, _map)
        trans.append(seed)

    return trans


def almanac(lines, seeds):
    # get soil, fertilizer, water, light, temp, humidity, location map
    seed_soil_map = get_maps(lines, 'seed-to-soil map:', 'soil-to-fertilizer map:')
    soil_fertilizer_map = get_maps(lines, 'soil-to-fertilizer map:', 'fertilizer-to-water map:')
    fertilizer_water_map = get_maps(lines, 'fertilizer-to-water map:', 'water-to-light map:')
    water_light_map = get_maps(lines, 'water-to-light map:', 'light-to-temperature map:')
    light_temp_map = get_maps(lines, 'light-to-temperature map:', 'temperature-to-humidity map:')
    temp_humidity_map = get_maps(lines, 'temperature-to-humidity map:', 'humidity-to-location map:')
    humidity_location_map = get_maps(lines, 'humidity-to-location map:', 'end')

    # get seeds mapped to maps
    soil = next_map(seeds, seed_soil_map)
    fertilizer = next_map(soil, soil_fertilizer_map)
    water = next_map(fertilizer, fertilizer_water_map)
    light = next_map(water, water_light_map)
    temp = next_map(light, light_temp_map)
    humidity = next_map(temp, temp_humidity_map)
    location = next_map(humidity, humidity_location_map)

    location_min = min(location)

    return location_min


def get_bisec_values(group):
    min_seed, r = group
    mid_s = [int((min_seed + min_seed + r) / 2)]
    max_s = [min_seed + r]
    min_s = [min_seed]

    return min_s, mid_s, max_s


def bisec_mdm(seeds, lines):
    seed_range = [(seeds[i], seeds[i + 1]) for i in range(0, len(seeds), 2)]
    ic(seed_range)
    for group in seed_range:
        ic('initial group', group)
        min_s, mid_s, max_s = get_bisec_values(group)

        ic('#1', min_s, mid_s, max_s, group)

        locations = []
        location_min_s = almanac(lines, min_s)
        location_mid_s = almanac(lines, mid_s)
        location_max_s = almanac(lines, max_s)
        ic('#2', location_min_s, location_mid_s, location_max_s)

        locations.append(location_max_s)
        locations.append(location_min_s)
        locations.append(location_mid_s)
        ic(locations)
        locations.sort()  # smallest location [0]
        ic('ord_locations', locations)

        group = (locations[0], locations[1])
        ic(group)
        min_s, mid_s, max_s = get_bisec_values(group)

        ic('#3', min_s, mid_s, max_s, group)

    return seeds


if __name__ == '__main__':
    lines, seeds = parse_input()
    seeds = bisec_mdm(seeds, lines)
