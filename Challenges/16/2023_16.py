import utils.advent as advent

advent.setup(2023, 16)


def parse_input(lines):
    return lines


def part1(lines):
    return 0


def part2(lines):
    return 0


if __name__ == "__main__":
    with open("Challenges/16/2023_16_debug.txt", "r") as file:
        lines = file.read().splitlines()
    # with advent.get_input() as file:
    #     lines = file.read().splitlines()

    print("############### Day 16 ###############")
    advent.print_answer(1, part1(lines))
    advent.print_answer(2, part2(lines))
