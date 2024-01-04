from icecream import ic


def win_sum(no_wins):
    win_sum = 0
    for win in no_wins:
        if win == 0:
            pass
        else:
            win_sum += 2 ** (win - 1)

    return int(win_sum)


def find_winning_ticket():
    # lines = open("test_input.txt").read().splitlines()
    lines = open("input.txt").read().splitlines()

    scratch_cards = []
    for card in lines:
        ticket, my_num = card.split('| ')
        my_num = list(map(int, my_num.split()))
        card_num, ticket_num = ticket.split(': ')
        ticket_num = list(map(int, ticket_num.split()))

        win_num = []
        for num in my_num:
            if num in ticket_num:
                win_num.append(num)

        win_fig = len(win_num)

        scratch_cards.append([card_num, win_fig])

        no_wins = []
        for card in scratch_cards:
            no_wins.append(card[1])

        result = win_sum(no_wins)

    return result, no_wins


def scratch_total(no_wins):
    cards = []
    for card_id, win in enumerate(no_wins):
        cards.append((card_id, win))

    idx = 0
    while idx < len(cards):
        card, win = cards[idx]
        idx += 1

        if win:
            cards += cards[card + 1: card + 1 + win]

    return idx


if __name__ == '__main__':
    win, no_wins = find_winning_ticket()
    ic(scratch_total(no_wins))
