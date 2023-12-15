import regex as re
import utils.advent as advent

advent.setup(2023, 4)


def parse_input(line):
    real_input = line.split(":")[-1]

    winning = real_input.split("|")[0]
    own = real_input.split("|")[1]

    winning_list = re.findall(r"\d+", winning)
    own_list = re.findall(r"\d+", own)

    return winning_list, own_list


def check_winning(line):
    winning_list, own_list = parse_input(line)

    counter = 0
    for n in own_list:
        if n in winning_list:
            counter += 1

    if counter == 0:
        return 0
    return pow(2, counter - 1)


def check_winning_pt2(line):
    winning_list, own_list = parse_input(line)

    counter = 0
    for n in own_list:
        if n in winning_list:
            counter += 1
    return counter


def part1(lines):
    counter = 0
    for l in lines:
        counter += check_winning(l)

    return counter


def part2(lines):
    list_of_lines = [1 for _ in range(len(lines))]
    for i, l in enumerate(lines):
        wins = check_winning_pt2(l)
        for idx in range(wins):
            try:
                list_of_lines[i + idx + 1] = (
                    list_of_lines[i + idx + 1] + list_of_lines[i]
                )
            except:
                pass

    return sum(list_of_lines)


if __name__ == "__main__":
    with advent.get_input() as file:
        lines = file.read().splitlines()

    print("############### Day 4 ###############")
    advent.submit_answer(1, part1(lines))
    advent.submit_answer(2, part2(lines))
