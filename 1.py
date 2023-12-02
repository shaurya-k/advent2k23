def part_one():
    with open("r.txt") as file:
        sum = 0
        for line in file:
            first_num = ""
            second_num = ""
            for char in line:
                if char.isnumeric():
                    if first_num == "":
                        first_num = int(char)
                    else:
                        second_num = int(char)
            if second_num == "":
                to_add = (first_num * 10) + first_num
            else:
                to_add = (first_num * 10) + second_num
            sum += to_add
    print(sum)  # 55002


def part_two():
    mapping = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9}
    with open("r.txt") as file:
        sum = 0
        for line in file:
            number_occurence_map = dict()
            for word in mapping.keys():
                word_len = len(word)
                for i in range(len(line)):
                    if i in number_occurence_map:
                        continue
                    elif line[i].isnumeric():
                        number_occurence_map[i] = 0
                    elif (line[i:i + word_len]) == word:
                        number_occurence_map[i] = word_len
            if len(number_occurence_map) == 1:
                for key, value in number_occurence_map.items():
                    if value == 0:
                        to_add = int(line[key]) * 10 + int(line[key])
                    else:
                        to_add = mapping[line[key:key + value]] * 10 + mapping[line[key:key + value]]
                sum += to_add
            else:
                first_num_key = min(number_occurence_map.keys())
                second_num_key = max(number_occurence_map.keys())
                len_first_num = number_occurence_map[first_num_key]
                len_second_num = number_occurence_map[second_num_key]

                if len_first_num == 0:
                    first_num = int(line[first_num_key]) * 10
                else:
                    first_num = mapping[line[first_num_key:first_num_key + len_first_num]] * 10

                if len_second_num == 0:
                    second_num = int(line[second_num_key])
                else:
                    second_num = mapping[line[second_num_key:second_num_key + len_second_num]]

                sum += first_num + second_num
        print(sum)  # 55093


if __name__ == "__main__":
    part_one()
    part_two()
