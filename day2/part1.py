from icecream import ic


def split_games():
    with open('input.txt') as f:
        lines = f.read().splitlines()
        rgb_rules = {'red': 12, 'green': 13, 'blue': 14}
        games = []

    for line in lines:
        cube_set = {'red': [], 'green': [], 'blue': []}
        game, plays = line.split(':')  # game = line.split(':')[0] plays = line.split(':')[1]
        game_id = game.replace('Game ', '')  # get game_id -> end sum
        single_play = plays.split(';')
        for _set in single_play:
            rgb_cube_set = _set.split(',')
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
        if cube_set_red <= rgb_rules['red'] and cube_set_blue <= rgb_rules['blue'] and cube_set_green <= rgb_rules[
            'green']:
            games.append(game_id)

    return games


def sum_games(games):
    result = 0
    for game in games:
        result += int(game)

    return result


if __name__ == '__main__':
    games = split_games()
    result = sum_games(games)
    ic(result)
