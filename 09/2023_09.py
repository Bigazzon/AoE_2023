import math
import utils.advent as advent

advent.setup(2023, 9)


def parse_input(lines):
    lines = [l.split() for l in lines]
    return [[int(c) for c in l] for l in lines]


def part1(lines):
    lines = parse_input(lines)
    counter = 0

    for l in lines:
        current_level = l
        last_values = []
        while True:
            new_level = [
                current_level[i] - current_level[i - 1]
                for i in range(1, len(current_level))
            ]
            last_values.append(current_level[-1])
            current_level = new_level
            if not any(new_level):
                break

        for v in last_values:
            counter += v

    return counter


def part2(lines):
    lines = parse_input(lines)
    counter = 0

    lines = lines[::-1]

    for l in lines:
        current_level = l
        first_values = []
        while True:
            new_level = [
                current_level[i] - current_level[i - 1]
                for i in range(1, len(current_level))
            ]
            first_values.append(current_level[0])
            current_level = new_level
            if not any(new_level):
                break

        list_counter = 0
        for v in first_values[::-1]:
            list_counter = v - list_counter
        counter += list_counter
    return counter


if __name__ == "__main__":
    # with open("09/2023_09_debug.txt", "r") as file:
    #     lines = file.read().splitlines()
    with advent.get_input() as file:
        lines = file.read().splitlines()

    print("############### Day 9 ###############")
    advent.submit_answer(1, part1(lines))
    advent.submit_answer(2, part2(lines))
