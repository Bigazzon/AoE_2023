import utils.advent as advent

advent.setup(2023, 18)

MOVE_MAP = {
    "L": [0, -1],
    "R": [0, 1],
    "U": [-1, 0],
    "D": [1, 0],
}

NUM_MAP = {0: "R", 1: "D", 2: "L", 3: "U"}


def parse_input(lines):
    new_lines = [l.split() for l in lines]
    return new_lines


def compute_area(coords):
    n = len(coords)  # number of coordinates
    area = 0.0
    for i in range(n):
        area += coords[i][0] * (coords[(i + 1) % n][1] - coords[(i - 1) % n][1])
    area = abs(area)
    return int(area / 2)


def convert_hex(hex):
    return int(str(hex), 16)


def part1(lines):
    lines = parse_input(lines)

    new_c = [0, 0]
    coords = [new_c]
    perimeter = 0
    for l in lines:
        new_c = [
            new_c[0] + int(l[1]) * MOVE_MAP[l[0]][0],
            new_c[1] + int(l[1]) * MOVE_MAP[l[0]][1],
        ]
        coords += [new_c]
        perimeter += int(l[1])

    return compute_area(coords) + int(perimeter / 2) + 1


def part2(lines):
    lines = parse_input(lines)

    new_c = [0, 0]
    coords = [new_c]
    perimeter = 0
    for l in lines:
        length = convert_hex(l[2][2:-2])

        new_c = [
            new_c[0] + length * MOVE_MAP[NUM_MAP[int(l[2][-2])]][0],
            new_c[1] + length * MOVE_MAP[NUM_MAP[int(l[2][-2])]][1],
        ]
        coords += [new_c]
        perimeter += length

    return compute_area(coords) + int(perimeter / 2) + 1


if __name__ == "__main__":
    # with open("challenges/18/2023_18_debug.txt", "r") as file:
    #     lines = file.read().splitlines()
    with advent.get_input() as file:
        lines = file.read().splitlines()

    print("############### Day 18 ###############")
    advent.submit_answer(1, part1(lines))
    advent.submit_answer(2, part2(lines))
