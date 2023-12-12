import math
import re
import utils.advent as advent

advent.setup(2023, 8)

MOVES_MAPPING = {"L": 0, "R": 1}


def lcm(a, cycle_steps):
    a = [cycle_steps[i] - a[i] for i in range(len(a))]
    res = 1
    for num in a:
        res = (num * res) // math.gcd(num, res)
    return res


def parse_input(lines):
    moves = lines[0]
    steps_dict = {}
    for l in lines[1:]:
        if l == "":
            continue
        starting, ending = l.split(" = ")
        steps_dict[starting] = re.findall(r"\w+", ending)
    return moves, steps_dict


def part1(lines):
    moves, steps_dict = parse_input(lines)
    initial_moves = [c for c in moves]
    moves = initial_moves.copy()
    current_node = "AAA"

    moves_counter = 0
    while len(moves) > 0:
        move = MOVES_MAPPING[moves.pop(0)]
        current_node = steps_dict[current_node][move]
        moves_counter += 1

        if current_node == "ZZZ":
            break

        if len(moves) == 0:
            moves += initial_moves
    return moves_counter


def part2(lines):
    moves, steps_dict = parse_input(lines)
    initial_moves = [c for c in moves]
    moves = initial_moves.copy()
    current_nodes = [start for start in steps_dict.keys() if start.endswith("A")]

    first_goals = ["" for _ in current_nodes]
    found_steps = [[] for _ in current_nodes]
    cycle_steps = [None for _ in current_nodes]

    moves_counter = 0
    while len(moves) > 0:
        move = MOVES_MAPPING[moves.pop(0)]
        moves_counter += 1
        for idx, n in enumerate(current_nodes):
            if cycle_steps[idx]:
                continue
            current_nodes[idx] = steps_dict[n][move]
            if current_nodes[idx].endswith("Z"):
                if current_nodes[idx] == first_goals[idx]:
                    cycle_steps[idx] = moves_counter
                if first_goals[idx] == "":
                    first_goals[idx] = current_nodes[idx]
                found_steps[idx].append(moves_counter)

        if all(cycle_steps):
            break
        if len(moves) == 0:
            moves += initial_moves

    return lcm([step[0] for step in found_steps], cycle_steps)


if __name__ == "__main__":
    # with open("08/2023_08_debug.txt", "r") as file:
    #     lines = file.read().splitlines()
    with advent.get_input() as file:
        lines = file.read().splitlines()

    print("############### Day 8 ###############")
    advent.submit_answer(1, part1(lines))
    advent.submit_answer(2, part2(lines))
