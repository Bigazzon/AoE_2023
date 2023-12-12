import numpy as np
import re
import utils.advent as advent

advent.setup(2023, 11)


def parse_input(lines, multiplier=2):
    x_pos, y_pos = [], []
    empty_x, empty_y = [], []
    transposed_lines = ["" for _ in range(len(lines[0]))]
    for idx, l in enumerate(lines):
        for i in range(len(l)):
            transposed_lines[i] = transposed_lines[i] + l[i]

        xs = [galaxy.start() for galaxy in re.finditer("#", l)]
        if len(xs) == 0:
            empty_x.append(idx)
            continue
        x_pos.extend(xs)
        y_pos.extend([idx] * len(xs))

    for idx, l in enumerate(transposed_lines):
        if re.search("#", l) is None:
            empty_y.append(idx)

    positions = [[x, y] for x, y in zip(y_pos, x_pos)]
    for i in range(len(positions)):
        positions[i] = [
            positions[i][0]
            + ((multiplier - 1) * np.sum(np.array(empty_x) < positions[i][0])),
            positions[i][1]
            + ((multiplier - 1) * np.sum(np.array(empty_y) < positions[i][1])),
        ]

    return positions


def part1(lines):
    galaxy_pos = parse_input(lines)
    counter = 0
    for i in range(len(galaxy_pos) - 1):
        for j in range(i + 1, len(galaxy_pos)):
            dist = abs((galaxy_pos[i][0] - galaxy_pos[j][0])) + abs(
                (galaxy_pos[i][1] - galaxy_pos[j][1])
            )
            counter += dist
    return counter


def part2(lines):
    galaxy_pos = parse_input(lines, 1000000)
    counter = 0
    for i in range(len(galaxy_pos) - 1):
        for j in range(i + 1, len(galaxy_pos)):
            dist = abs((galaxy_pos[i][0] - galaxy_pos[j][0])) + abs(
                (galaxy_pos[i][1] - galaxy_pos[j][1])
            )
            counter += dist
    return counter


if __name__ == "__main__":
    # with open("11/2023_11_debug.txt", "r") as file:
    #     lines = file.read().splitlines()
    with advent.get_input() as file:
        lines = file.read().splitlines()

    print("############### Day 11 ###############")
    advent.submit_answer(1, part1(lines))
    advent.submit_answer(2, part2(lines))
