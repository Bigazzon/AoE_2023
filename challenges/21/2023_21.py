import utils.advent as advent
import numpy as np

advent.setup(2023, 21)

MOVE_MAP = {
    "L": [0, -1],
    "R": [0, 1],
    "U": [-1, 0],
    "D": [1, 0],
}


def parse_input(lines):
    rocks = set()
    for i, l in enumerate(lines):
        for j, c in enumerate(l):
            if c == "S":
                s = (i, j)
            elif c == "#":
                rocks.add((i, j))
    return lines, s, rocks


def part1(lines):
    lines, s, rocks = parse_input(lines)
    steps = 64
    positions = set([s])
    for i in range(steps):
        new_positions = set()
        for pos in positions:
            for d in MOVE_MAP.values():
                new_pos = (pos[0] + d[0], pos[1] + d[1])
                if new_pos[0] < 0 or new_pos[1] < 0:
                    continue
                if new_pos[0] > len(lines) or new_pos[1] > len(lines[0]):
                    continue
                if new_pos not in rocks:
                    new_positions.add(new_pos)
        positions = new_positions
    return len(positions)


P = complex


class Grid:
    def __init__(self, input):
        self.size = len(input)
        self.grid = set()
        self.positions = set()
        for y, l in enumerate(input):
            for x, v in enumerate(l):
                if v == "#":
                    self.grid.add(P(x, y))
                if v == "S":
                    self.positions.add(P(x, y))

    def step(self):
        newPos = set()
        for p in self.positions:
            for d in (1, -1, 1j, -1j):
                if self.wrap(p + d) not in self.grid:
                    newPos.add(p + d)
        self.positions = newPos

    def wrap(self, p):
        return P(p.real % self.size, p.imag % self.size)


def part2(lines):
    lines, s, rocks = parse_input(lines)
    steps = 26501365
    positions = set([s])
    length = len(lines)
    x, y = [0, 1, 2], []
    repetitions = (steps - length // 2) // length
    for s in range(length // 2 + length * 2 + 1):
        if s % length == length // 2:
            y.append(len(positions))

        new_positions = set()
        for pos in positions:
            for d in MOVE_MAP.values():
                new_pos = (pos[0] + d[0], pos[1] + d[1])
                new_pos_filtered = (new_pos[0] % length, new_pos[1] % length)
                if new_pos_filtered not in rocks:
                    new_positions.add(new_pos)
        positions = new_positions
    poly = np.rint(np.polynomial.polynomial.polyfit(x, y, 2)).astype(int).tolist()
    return int(sum(poly[i] * repetitions**i for i in range(3)))


if __name__ == "__main__":
    # with open("challenges/21/2023_21_debug.txt", "r") as file:
    #     lines = file.read().splitlines()
    with advent.get_input() as file:
        lines = file.read().splitlines()

    print("############### Day 21 ###############")
    advent.submit_answer(1, part1(lines))
    advent.submit_answer(2, part2(lines))
