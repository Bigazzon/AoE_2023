import utils.advent as advent

advent.setup(2023, 22)


def parse_input(lines):
    return lines


def part1(lines):
    lines = parse_input(lines)
    return 0


def part2(lines):
    lines = parse_input(lines)
    return 0


if __name__ == "__main__":
    # with open("challenges/22/2023_22_debug.txt", "r") as file:
    #     lines = file.read().splitlines()
    with advent.get_input() as file:
        lines = file.read().splitlines()

    print("############### Day 22 ###############")
    advent.submit_answer(1, part1(lines))
    advent.submit_answer(2, part2(lines))