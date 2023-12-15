from functools import cache
import regex as re
import utils.advent as advent
from tqdm import tqdm

advent.setup(2023, 12)


def parse_input(lines):
    symbs, nums = [], []
    for l in lines:
        symbols, num_list = l.split(" ")
        num_list = re.findall(r"(\d+)", l)
        symbs.append(symbols)
        nums.append([int(n) for n in num_list])
    return [[s, n] for s, n in zip(symbs, nums)]


@cache
def count_possibilities(
    string,
    nums,
):
    size = len(string)
    if len(nums) == 0:
        if string == "":
            return 1
        if all(c in ".?" for c in string):
            return 1
        return 0

    curr = nums[0]
    others = nums[1:]
    after = sum(others) + len(others)

    counter = 0

    for before in range(size - after - curr + 1):
        cand = "." * before + "#" * curr + "."
        if all(s == c or s == "?" for c, s in zip(cand, string)):
            counter += count_possibilities(string[len(cand) :], others)

    return counter


@cache
def find_arrangements(string, nums, copies=1):
    counter = 0
    string = "?".join([string] * copies)
    nums = nums * copies
    counter += count_possibilities(string, nums)
    return counter


def part1(lines):
    lines = parse_input(lines)
    counter = 0
    for s, n in lines:
        counter += find_arrangements(s, tuple(n))
    return counter


def part2(lines):
    lines = parse_input(lines)
    counter = 0
    for s, n in tqdm(lines):
        counter += find_arrangements(s, tuple(n), copies=5)
    return counter


if __name__ == "__main__":
    with open("challenges/12/2023_12_debug.txt", "r") as file:
        lines = file.read().splitlines()
    with advent.get_input() as file:
        lines = file.read().splitlines()

    print("############### Day 12 ###############")
    advent.submit_answer(1, part1(lines))
    advent.submit_answer(2, part2(lines))
