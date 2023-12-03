grid = []


def check_for_symbol(i, j_checks):
    # x x x x x
    # x 1 2 3 x
    # x x x x x
    neighbors = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, -1), (-1, 1)]

    for ind in j_checks:
        for neighbor in neighbors:
            x, y = neighbor
            if check_spot(i + x, ind + y):
                return True
    return False


def check_spot(i, j):
    symbols = ['$', '&', '/', '@', '-', '%', '#', '*', '+', '=']
    try:
        if grid[i][j] in symbols:
            return True
    except IndexError:
        return False
    return False


def part_one():
    sum = 0
    with open("r.txt") as file:
        for line in file:
            grid.append(list(line))

        for i in range(len(grid)):
            str_num = ""
            j_checks = []
            for j in range(len(grid[i])):
                if grid[i][j].isdigit():
                    str_num += grid[i][j]
                    j_checks.append(j)
                elif str_num != "":
                    if check_for_symbol(i, j_checks):
                        sum += int(str_num)
                    str_num = ""
                    j_checks = []

    print(sum)  # 540131


def check_spot_for_number(i, j):
    if grid[i][j].isdigit():
        str_num = ""
        # go back til first digit is found
        while j - 1 >= 0 and grid[i][j - 1].isdigit():
            j -= 1
        while j <= len(grid[0]) and grid[i][j].isdigit():
            str_num += grid[i][j]
            j += 1
        print(str_num)
        return True, int(str_num)

    return False, 1


def check_for_numbers(i, j):
    # x x x
    # x * x
    # x x x
    nums = set()
    neighbors = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, -1), (-1, 1)]
    for neighbor in neighbors:
        x, y = neighbor
        found, num = check_spot_for_number(i + x, j + y)
        if found:
            nums.add(num)
    if len(nums) > 1:
        gear = 1
        for num in nums:
            gear *= num
        return gear
    return 0


def part_two():
    sum = 0
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == "*":
                sum += check_for_numbers(i, j)

    print(sum)  # 86879020


if __name__ == "__main__":
    part_one()
    part_two()
