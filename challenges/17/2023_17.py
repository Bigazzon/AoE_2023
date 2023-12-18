import utils.advent as advent
from queue import PriorityQueue

advent.setup(2023, 17)

NORTH = (-1, 0)
SOUTH = (1, 0)
EAST = (0, 1)
WEST = (0, -1)


def parse_input(lines):
    new_lines = [[] for _ in range(len(lines))]
    for i, l in enumerate(lines):
        new_lines[i] = [int(c) for c in l]
    return new_lines


def compute_minimum_cost(lines, min_moves=1, max_moves=3):
    q = PriorityQueue()

    visited = set()
    q.put((0, 0, 0, 0, 0, 0))

    while q.qsize() > 0:
        weight, r, c, dr, dc, n = q.get()

        if r == len(lines) - 1 and c == len(lines[0]) - 1 and n >= min_moves:
            return weight

        if (r, c, dr, dc, n) in visited:
            continue

        visited.add((r, c, dr, dc, n))

        if n < max_moves and (dr, dc) != (0, 0):
            nr = r + dr
            nc = c + dc
            if 0 <= nr < len(lines) and 0 <= nc < len(lines[0]):
                q.put((weight + lines[nr][nc], nr, nc, dr, dc, n + 1))

        if n >= min_moves or (dr, dc) == (0, 0):
            for ndr, ndc in [NORTH, SOUTH, EAST, WEST]:
                if (ndr, ndc) != (dr, dc) and (ndr, ndc) != (-dr, -dc):
                    nr = r + ndr
                    nc = c + ndc
                    if 0 <= nr < len(lines) and 0 <= nc < len(lines[0]):
                        q.put((weight + lines[nr][nc], nr, nc, ndr, ndc, 1))


def part1(lines):
    lines = parse_input(lines)
    cost = compute_minimum_cost(lines)
    return cost


def part2(lines):
    lines = parse_input(lines)
    cost = compute_minimum_cost(lines, min_moves=4, max_moves=10)
    return cost


if __name__ == "__main__":
    # with open("challenges/17/2023_17_debug.txt", "r") as file:
    #     lines = file.read().splitlines()
    with advent.get_input() as file:
        lines = file.read().splitlines()

    print("############### Day 17 ###############")
    advent.submit_answer(1, part1(lines))
    advent.submit_answer(2, part2(lines))
