import utils.advent as advent

advent.setup(2023, 10)

MOVE_MAPPING = {
    "F": [6, 8],
    "7": [4, 8],
    "J": [2, 4],
    "L": [2, 6],
    "|": [2, 8],
    "-": [4, 6],
}

POS_MAPPING = {2: [-1, 0], 4: [0, -1], 6: [0, 1], 8: [1, 0]}


def parse_input(lines):
    output = []
    for i, l in enumerate(lines):
        output.append([c for c in l])
        if "S" in l:
            pos = [i, l.index("S")]
    return output, pos


def check_connection(move, curr, new):
    if move == ".":
        return False

    delta = [curr[0] - new[0], curr[1] - new[1]]
    accepted = [POS_MAPPING[m] for m in MOVE_MAPPING[move]]

    return delta in accepted


def find_starting_connections(tubes, pos):
    start1, start2 = None, None

    for move in [2, 4, 6, 8]:
        new_pos = [pos[0] + POS_MAPPING[move][0], pos[1] + POS_MAPPING[move][1]]
        if not check_pos(tubes, new_pos):
            continue
        if not check_connection(tubes[new_pos[0]][new_pos[1]], pos, new_pos):
            continue
        if tubes[new_pos[0]][new_pos[1]] != "." and start1 is None:
            start1 = new_pos
        elif tubes[new_pos[0]][new_pos[1]] != ".":
            start2 = new_pos

    return start1, start2


def check_pos(tubes, pos):
    max_x = len(tubes[0])
    max_y = len(tubes)
    return not (pos[0] < 0 or pos[0] >= max_y or pos[1] < 0 or pos[1] >= max_x)


def compute_new_pos(tubes, distances, curr):
    delta = [POS_MAPPING[m] for m in MOVE_MAPPING[tubes[curr[0]][curr[1]]]]

    for d in delta:
        new_pos = [curr[0] + d[0], curr[1] + d[1]]
        if distances[new_pos[0]][new_pos[1]] == False:
            return new_pos
    raise Exception("No new position found")


def part1(lines):
    tubes, start = parse_input(lines)
    distances = [[False for _ in range(len(lines[0]))] for _ in range(len(lines))]
    distances[start[0]][start[1]] = True

    start1, start2 = find_starting_connections(tubes, start)
    distances[start1[0]][start1[1]] = True
    distances[start2[0]][start2[1]] = True

    max_moves = 1
    while True:
        start1, start2 = compute_new_pos(tubes, distances, start1), compute_new_pos(
            tubes, distances, start2
        )
        distances[start1[0]][start1[1]] = True
        distances[start2[0]][start2[1]] = True
        max_moves += 1
        if start1 == start2:
            break
    return max_moves


def part2(lines):
    tubes, start = parse_input(lines)
    distances = [[False for _ in range(len(lines[0]))] for _ in range(len(lines))]
    distances[start[0]][start[1]] = True

    start1, start2 = find_starting_connections(tubes, start)
    distances[start1[0]][start1[1]] = True
    distances[start2[0]][start2[1]] = True

    while True:
        start1, start2 = compute_new_pos(tubes, distances, start1), compute_new_pos(
            tubes, distances, start2
        )
        distances[start1[0]][start1[1]] = True
        distances[start2[0]][start2[1]] = True
        if start1 == start2:
            break

    counter = 0
    checking_symb = None
    debug_map = [[0 for _ in range(len(lines[0]))] for _ in range(len(lines))]
    for i in range(len(tubes)):
        state = 0
        for j in range(len(tubes[0])):
            if tubes[i][j] == "." or distances[i][j] == False:
                debug_map[i][j] = int(state)
                counter += state

            if checking_symb:
                if distances[i][j] == True:
                    if tubes[i][j] != "-" and tubes[i][j] != checking_symb:
                        checking_symb = None
                    if tubes[i][j] == checking_symb:
                        checking_symb = None
                        state = 1 - state

            if checking_symb is None:
                if tubes[i][j] == "|" and distances[i][j] == True:
                    checking_symb = None
                    state = 1 - state
                elif tubes[i][j] == "F" and distances[i][j] == True:  # ----J
                    checking_symb = "J"
                elif tubes[i][j] == "L" and distances[i][j] == True:  # ----7
                    checking_symb = "7"

    return counter


if __name__ == "__main__":
    # with open("Challenges/10/2023_10_debug.txt", "r") as file:
    #     lines = file.read().splitlines()
    with advent.get_input() as file:
        lines = file.read().splitlines()

    print("############### Day 10 ###############")
    advent.submit_answer(1, part1(lines))
    advent.submit_answer(2, part2(lines))
