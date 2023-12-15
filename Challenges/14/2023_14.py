from collections import deque
from tqdm import tqdm
import utils.advent as advent

advent.setup(2023, 14)


def transpose_lines(lines):
    return ["".join(t) for t in zip(*lines)]


def rotate_counterclockwise(lines):
    new_lines = ["" for _ in range(len(lines))]
    for i, l in enumerate(lines):
        for j, c in enumerate(l[::-1]):
            new_lines[j] += c
    return new_lines


def rotate_clockwise(lines):
    new_lines = ["" for _ in range(len(lines))]
    for i, l in enumerate(lines[::-1]):
        for j, c in enumerate(l):
            new_lines[j] += c
    return new_lines


def extract_rocks(lines):
    round = [[0] for _ in range(len(lines))]
    square = [[0] for _ in range(len(lines))]
    for i, l in enumerate(lines):
        for idx, c in enumerate(l):
            if c == "#":
                square[i].append(idx + 1)
                round[i].append(0)
            elif c == "O":
                round[i][len(square[i]) - 1] += 1
    return round, square


def new_count_output(lines):
    length = len(lines)
    counter = 0
    for i, l in enumerate(lines):
        for _, c in enumerate(l):
            if c == "O":
                counter += length - i
    return counter


def count_output(round, square, length):
    counter = 0
    for r, s in zip(round, square):
        for i in range(len(r)):
            if r[i] == 0:
                continue
            for j in range(r[i]):
                counter += length - s[i] - j
    return counter


def recompute_lines(lines, round, square):
    new_lines = [["."] * len(lines[0]) for _ in range(len(lines))]
    for i in range(len(round)):
        for j in range(len(round[i])):
            for k in range(round[i][j]):
                new_lines[i][square[i][j] + k] = "O"
        for j in range(len(square[i][1:])):
            new_lines[i][square[i][j + 1] - 1] = "#"
    new_lines = ["".join(l) for l in new_lines]
    new_lines = transpose_lines(new_lines)
    return new_lines


def part1(lines):
    lines = transpose_lines(lines)
    round, square = extract_rocks(lines)
    return count_output(round, square, len(lines[0]))


def part2(lines):
    cycles = 1000000000
    init_lines = deque(maxlen=cycles)
    loop_length = 0
    for cyc in range(cycles):
        init_lines.append(lines.copy())
        for _ in range(4):
            lines = transpose_lines(lines)
            round, square = extract_rocks(lines)
            lines = recompute_lines(lines, round, square)
            lines = rotate_clockwise(lines)

        for i, init in enumerate(init_lines):
            if lines == init:
                loop_length = len(init_lines) - i
                break
        if loop_length:
            break
    remainder = (cycles - cyc) % loop_length

    return new_count_output(init_lines[-loop_length + remainder - 1])


if __name__ == "__main__":
    # with open("Challenges/14/2023_14_debug.txt", "r") as file:
    #     lines = file.read().splitlines()
    with advent.get_input() as file:
        lines = file.read().splitlines()

    print("############### Day 14 ###############")
    advent.submit_answer(1, part1(lines))
    advent.submit_answer(2, part2(lines))
