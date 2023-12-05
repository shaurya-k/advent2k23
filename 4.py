def part_one():
    sum = 0
    with open("r.txt") as file:
        for line in file:
            line = line.strip().split(':')
            card_info = line[0]
            card_info = card_info[4:].strip()
            card_num = int(card_info)
            card_games = line[1].split('|')
            winning_nums = card_games[0].strip().split()
            winning_nums_set = {int(a) for a in winning_nums}

            draw_nums = card_games[1].strip().split()
            to_add = 0
            for a in draw_nums:
                if int(a) in winning_nums_set:
                    if to_add == 0:
                        to_add = 1
                    else:
                        to_add *= 2
            sum += to_add

    print(sum)  # 24706


def part_two():
    sum = 0
    rounds = {}
    with open("r.txt") as file:
        for line in file:
            line = line.strip().split(':')
            card_info = line[0]
            card_info = card_info[4:].strip()
            card_num = int(card_info)
            if card_num not in rounds:
                rounds[card_num] = 1
            card_games = line[1].split('|')
            winning_nums = card_games[0].strip().split()
            winning_nums_set = {int(a) for a in winning_nums}

            draw_nums = card_games[1].strip().split()
            matches = 0

            for a in draw_nums:
                if int(a) in winning_nums_set:
                    matches += 1

            for a in range(card_num + 1, card_num + matches + 1):
                rounds[a] = rounds.get(a, 1) + rounds[card_num]

        for k in rounds:
            sum += rounds[k]
    print(sum)  # 13114317


if __name__ == "__main__":
    part_one()
    part_two()
