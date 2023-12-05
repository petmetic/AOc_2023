from icecream import ic
import re


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
            # ic('#1', seed, s, d, seed - s + d)
            seed = seed - s + d
            return seed
        # ic('#2', seed)
    return seed


def next_map(seeds, _map):
    trans = []
    for seed in seeds:
        seed = get_stencil(seed, _map)
        trans.append(seed)

    return trans


def almanac():
    # lines = open("test_input.txt").read().splitlines()
    lines = open("input.txt").read().splitlines()

    # get seeds
    _, seeds = lines[0].split(': ')
    seeds = list(map(int, seeds.split()))

    # get soil, fertilizer, water, light, temp, humidity, location map
    seed_soil_map = get_maps(lines, 'seed-to-soil map:', 'soil-to-fertilizer map:')
    # ic(seed_soil_map)
    soil_fertilizer_map = get_maps(lines, 'soil-to-fertilizer map:', 'fertilizer-to-water map:')
    # ic(soil_fertilizer_map)
    fertilizer_water_map = get_maps(lines, 'fertilizer-to-water map:', 'water-to-light map:')
    # ic(fertilizer_water_map)
    water_light_map = get_maps(lines, 'water-to-light map:', 'light-to-temperature map:')
    # ic(water_light_map)
    light_temp_map = get_maps(lines, 'light-to-temperature map:', 'temperature-to-humidity map:')
    # ic(light_temp_map)
    temp_humidity_map = get_maps(lines, 'temperature-to-humidity map:', 'humidity-to-location map:')
    # ic(temp_humidity_map)
    humidity_location_map = get_maps(lines, 'humidity-to-location map:', 'end')
    # ic(humidity_location_map)
    # get seeds mapped to maps

    ic(seeds)
    soil = next_map(seeds, seed_soil_map)
    ic(soil)
    fertilizer = next_map(soil, soil_fertilizer_map)
    ic(fertilizer)
    ic('fertilizer-water map')
    water = next_map(fertilizer, fertilizer_water_map)
    ic(water)
    light = next_map(water, water_light_map)
    ic(light)
    temp = next_map(light, light_temp_map)
    ic(temp)
    humidity = next_map(temp, temp_humidity_map)
    ic(humidity)
    location = next_map(humidity, humidity_location_map)
    ic(location)

    result = min(location)

    return result


if __name__ == '__main__':
    result = almanac()
    ic(result)
