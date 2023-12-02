def part_one():
    with open("r.txt") as file:
        cubes_map = {"red": 12, "green": 13, "blue": 14}
        sum = 0
        for line in file:
            colon_index = line.index(':')
            game_id = int(line[5:colon_index])
            line = line[colon_index+2:len(line)]
            rounds = line.split(';')
            valid = True
            for round in rounds:
                round = round.strip()
                plays = round.split(',')
                for play in plays:
                    play = play.strip()
                    parse = play.split(" ")
                    if cubes_map[parse[1]] < int(parse[0]):
                        valid = False
                        break

            if valid:
                sum += game_id

    print(sum)  # 2061


def part_two():
    with open("r.txt") as file:
        sum = 0
        for line in file:
            colon_index = line.index(':')
            line = line[colon_index+2:len(line)]
            rounds = line.split(';')
            cubes_map = {"red": 1, "green": 1, "blue": 1}
            for round in rounds:
                round = round.strip()
                plays = round.split(',')
                for play in plays:
                    play = play.strip()
                    parse = play.split(" ")
                    if cubes_map[parse[1]] < int(parse[0]):
                        cubes_map[parse[1]] = int(parse[0])
            to_add = 1
            for k in cubes_map:
                to_add *= cubes_map[k]
            sum += to_add

    print(sum)  # 72596


if __name__ == "__main__":
    part_one()
    part_two()
