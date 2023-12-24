from collections import deque
import utils.advent as advent

advent.setup(2023, 22)


def parse_input(lines):
    new_lines = []
    for l in lines:
        start, end = l.split("~")
        new_lines.append(
            ([int(x) for x in start.split(",")], [int(x) for x in end.split(",")])
        )
    return new_lines


def check_overlap(a, b):
    return max(a[0][0], b[0][0]) <= min(a[1][0], b[1][0]) and max(
        a[0][1], b[0][1]
    ) <= min(a[1][1], b[1][1])


def part1(lines):
    bricks = parse_input(lines)
    bricks.sort(key=lambda brick: brick[0][2])

    for index, brick in enumerate(bricks):
        max_z = 1
        for other_brick in bricks[:index]:
            if check_overlap(brick, other_brick):
                max_z = max(max_z, other_brick[1][2] + 1)
        brick[1][2] -= brick[0][2] - max_z
        brick[0][2] = max_z

    bricks.sort(key=lambda brick: brick[0][2])

    i_on_j = {i: set() for i in range(len(bricks))}
    j_on_i = {i: set() for i in range(len(bricks))}

    for j, upper in enumerate(bricks):
        for i, lower in enumerate(bricks[:j]):
            if check_overlap(lower, upper) and upper[0][2] == lower[1][2] + 1:
                i_on_j[i].add(j)
                j_on_i[j].add(i)

    total = 0
    for i in range(len(bricks)):
        if all(len(j_on_i[j]) >= 2 for j in i_on_j[i]):
            total += 1
    return total


def part2(lines):
    bricks = parse_input(lines)
    bricks.sort(key=lambda brick: brick[0][2])

    for index, brick in enumerate(bricks):
        max_z = 1
        for other_brick in bricks[:index]:
            if check_overlap(brick, other_brick):
                max_z = max(max_z, other_brick[1][2] + 1)
        brick[1][2] -= brick[0][2] - max_z
        brick[0][2] = max_z

    bricks.sort(key=lambda brick: brick[0][2])

    i_on_j = {i: set() for i in range(len(bricks))}
    j_on_i = {i: set() for i in range(len(bricks))}

    for j, upper in enumerate(bricks):
        for i, lower in enumerate(bricks[:j]):
            if check_overlap(lower, upper) and upper[0][2] == lower[1][2] + 1:
                i_on_j[i].add(j)
                j_on_i[j].add(i)

    total = 0

    for i in range(len(bricks)):
        q = deque(j for j in i_on_j[i] if len(j_on_i[j]) == 1)
        falling_bricks = set(q)
        falling_bricks.add(i)

        while q:
            j = q.popleft()
            for k in i_on_j[j] - falling_bricks:
                if j_on_i[k] <= falling_bricks:
                    q.append(k)
                    falling_bricks.add(k)
        total += len(falling_bricks) - 1
    return total


if __name__ == "__main__":
    # with open("challenges/22/2023_22_debug.txt", "r") as file:
    #     lines = file.read().splitlines()
    with advent.get_input() as file:
        lines = file.read().splitlines()

    print("############### Day 22 ###############")
    advent.submit_answer(1, part1(lines))
    advent.submit_answer(2, part2(lines))
