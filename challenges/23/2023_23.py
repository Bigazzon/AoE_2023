from collections import deque
import utils.advent as advent

advent.setup(2023, 23)

SLOPES = {"^": [-1, 0], "v": [1, 0], "<": [0, -1], ">": [0, 1]}


def parse_input(lines):
    return lines


def dfs(coord, curr_dist, max_dist, seen, neighbors_map):
    height = len(seen)
    y, x = coord
    if seen[y][x]:
        return seen, max_dist
    seen[y][x] = True
    if y == height - 1:
        max_dist = max(max_dist, curr_dist)
    for pos, neighbors in neighbors_map[coord]:
        seen, max_dist = dfs(pos, curr_dist + neighbors, max_dist, seen, neighbors_map)
    seen[y][x] = False
    return seen, max_dist


def find_longest_path(grid, slopes=True):
    height = len(grid)
    width = len(grid[0])
    V = set()

    for x in range(width):
        if grid[0][x] == ".":
            V.add((0, x))
            start = (0, x)
        if grid[height - 1][x] == ".":
            V.add((height - 1, x))

    for y in range(height):
        for x in range(width):
            neighbors = 0
            for symbol, direction in SLOPES.items():
                dy, dx = direction
                if (
                    0 <= y + dy < height
                    and 0 <= x + dx < width
                    and grid[y + dy][x + dx] != "#"
                ):
                    neighbors += 1
            if neighbors > 2 and grid[y][x] != "#":
                V.add((y, x))

    neighbors_map = {}
    for pos_y, pos_x in V:
        neighbors_map[(pos_y, pos_x)] = []
        q = deque([(pos_y, pos_x, 0)])
        seen = set()
        while q:
            y, x, d = q.popleft()
            if (y, x) in seen:
                continue
            seen.add((y, x))
            if (y, x) in V and (y, x) != (pos_y, pos_x):
                neighbors_map[(pos_y, pos_x)].append(((y, x), d))
                continue
            for symbol, direction in SLOPES.items():
                dy, dx = SLOPES[symbol]
                if (
                    0 <= y + dy < height
                    and 0 <= x + dx < width
                    and grid[y + dy][x + dx] != "#"
                ):
                    if (
                        slopes
                        and grid[y][x] in ["<", ">", "^", "v"]
                        and grid[y][x] != symbol
                    ):
                        continue
                    q.append((y + dy, x + dx, d + 1))

    ans = 0
    seen = [[False for _ in range(width)] for _ in range(height)]
    seen, ans = dfs(start, 0, ans, seen, neighbors_map)
    return ans


def part1(lines):
    lines = parse_input(lines)
    grid = [[c for c in row] for row in lines]
    return find_longest_path(grid)


def part2(lines):
    lines = parse_input(lines)
    grid = [[c for c in row] for row in lines]
    return find_longest_path(grid, slopes=False)


if __name__ == "__main__":
    # with open("challenges/23/2023_23_debug.txt", "r") as file:
    #     lines = file.read().splitlines()
    with advent.get_input() as file:
        lines = file.read().splitlines()

    print("############### Day 23 ###############")
    advent.submit_answer(1, part1(lines))
    advent.submit_answer(2, part2(lines))
