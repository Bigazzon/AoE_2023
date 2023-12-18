from collections import deque
import utils.advent as advent

advent.setup(2023, 16)


NORTH = (-1, 0)
SOUTH = (1, 0)
EAST = (0, 1)
WEST = (0, -1)


def parse_input(lines):
    return lines


def count_cells(grid, start, direction):
    q = deque()
    l = start + direction
    q.append(l)
    visited = set()

    while q:
        l = q.popleft()
        pos, dir = l[:2], l[2:]
        if tuple((pos[0], pos[1])) not in grid or l in visited:
            continue
        visited.add(l)
        if grid[pos] == "/":
            dir = -dir[1], -dir[0]
            pos = (pos[0] + dir[0], pos[1] + dir[1])
            q.append(tuple((pos + dir)))
        elif grid[pos] == "\\":
            dir = dir[1], dir[0]
            pos = (pos[0] + dir[0], pos[1] + dir[1])
            q.append(tuple((pos + dir)))
        elif grid[pos] == "|" and dir[0] == 0:
            pos = (pos[0] + NORTH[0], pos[1] + NORTH[1])
            q.append(tuple((pos + NORTH)))
            pos = (pos[0] + SOUTH[0], pos[1] + SOUTH[1])
            q.append(tuple((pos + SOUTH)))
        elif grid[pos] == "-" and dir[1] == 0:
            pos = (pos[0] + EAST[0], pos[1] + EAST[1])
            q.append(tuple((pos + EAST)))
            pos = (pos[0] + WEST[0], pos[1] + WEST[1])
            q.append(tuple((pos + WEST)))
        else:
            pos = (pos[0] + dir[0], pos[1] + dir[1])
            q.append(tuple((pos + dir)))

    return len(set(pos[:2] for pos in visited))


def part1(lines):
    grid = {
        tuple((i, j)): x
        for i, row in enumerate(lines)
        for j, x in enumerate(row.strip())
    }
    return count_cells(grid, (0, 0), EAST)


def part2(lines):
    grid = {tuple((i, j)): x for i, row in enumerate(lines) for j, x in enumerate(row)}
    n, m = len(lines), len(lines[0])

    max_count = 0
    for i in range(n):
        max_count = max(max_count, count_cells(grid, (0, i), SOUTH))
        max_count = max(max_count, count_cells(grid, (n - 1, i), NORTH))
    for i in range(m):
        max_count = max(max_count, count_cells(grid, (i, 0), EAST))
        max_count = max(max_count, count_cells(grid, (i, m - 1), WEST))

    return max_count


if __name__ == "__main__":
    # with open("challenges/16/2023_16_debug.txt", "r") as file:
    #     lines = file.read().splitlines()
    with advent.get_input() as file:
        lines = file.read().splitlines()

    print("############### Day 16 ###############")
    advent.print_answer(1, part1(lines))
    advent.print_answer(2, part2(lines))
