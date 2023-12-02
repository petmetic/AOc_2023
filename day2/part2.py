from icecream import ic


def games_power():
    with open('input.txt') as f:
        lines = f.read().splitlines()
        games_power = []
    for line in lines:

        cube_set = {'red': [], 'green': [], 'blue': []}
        game, _sets = line.split(':')
        _set = _sets.split(';')
        for single_play in _set:
            rgb_cube_set = single_play.split(',')
            for rgb_cube in rgb_cube_set:
                count, color = rgb_cube.strip().split(' ')
                if color == 'red':
                    cube_set['red'].append(int(count))
                elif color == 'green':
                    cube_set['green'].append(int(count))
                else:
                    cube_set['blue'].append(int(count))
        cube_set_red = max(cube_set['red'])
        cube_set_blue = max(cube_set['blue'])
        cube_set_green = max(cube_set['green'])
        games_power.append(cube_set_red * cube_set_green * cube_set_blue)

    return games_power


if __name__ == '__main__':
    games = games_power()
    ic(sum(games))
