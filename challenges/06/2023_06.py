import regex as re
import math
import utils.advent as advent

advent.setup(2023, 6)


def parse_input(lines):
    times = [int(n) for n in re.findall(r"\d+", lines[0].split(":")[-1])]
    distances = [int(n) for n in re.findall(r"\d+", lines[1].split(":")[-1])]
    return times, distances


def parse_input_pt2(lines):
    times = re.findall(r"\d+", lines[0].split(":")[-1])
    distances = re.findall(r"\d+", lines[1].split(":")[-1])
    return int("".join(times)), int("".join(distances))


def winning_cases(time, distance):
    counter = 0
    for t in range(1, time):
        speed = t
        race_dist = speed * (time - t)
        if race_dist > distance:
            counter += 1
    return counter


def diseq_winning_cases(time, distance):
    pos = (time + math.sqrt(math.pow(time, 2) - 4 * distance)) / 2
    neg = (time - math.sqrt(math.pow(time, 2) - 4 * distance)) / 2
    return math.floor(pos) - math.ceil(neg) + 1


def part1(lines):
    times, distances = parse_input(lines)
    winning_cases_list = []
    for i in range(len(times)):
        winning_cases_list.append(diseq_winning_cases(times[i], distances[i]))
    return math.prod(winning_cases_list)


def part2(lines):
    time, distance = parse_input_pt2(lines)
    winning_case_number = diseq_winning_cases(time, distance)
    return winning_case_number


if __name__ == "__main__":
    # with open("challenges/06/2023_06_debug.txt", "r") as file:
    #     lines = file.read().splitlines()
    with advent.get_input() as file:
        lines = file.read().splitlines()

    print("############### Day 6 ###############")
    advent.submit_answer(1, part1(lines))
    advent.submit_answer(2, part2(lines))
