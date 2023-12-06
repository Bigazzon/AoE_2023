import regex as re
import utils.advent as advent

advent.setup(2023, 7)


def parse_input(lines):
    times = [int(n) for n in re.findall(r"\d+", lines[0].split(":")[-1])]
    distances = [int(n) for n in re.findall(r"\d+", lines[1].split(":")[-1])]
    return times, distances


def part1(lines):
    return 0


def part2(lines):
    return 0


if __name__ == "__main__":
    # with open("07/2023_07_debug.txt", "r") as file:
    #     lines = file.read().splitlines()
    with advent.get_input() as file:
        lines = file.read().splitlines()

    print("############### Day 7 ###############")
    
    advent.print_answer(1, part1(lines))
    advent.submit_answer(1, part1(lines))
    
    advent.print_answer(2, part2(lines))
    advent.submit_answer(2, part2(lines))
