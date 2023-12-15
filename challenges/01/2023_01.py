import regex as re
import utils.advent as advent

advent.setup(2023, 1)


def part1(lines):
    int_list = []
    for st in lines:
        int_list.append(re.findall(r"\d", st))
    counter = 0
    for num_list in int_list:
        counter += int(num_list[0] + num_list[-1])
    return counter


def part2(lines):
    NUMBER_NAMES = {
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9",
    }
    counter = 0
    for i, st in enumerate(lines):
        regexp_list = re.findall(r"\d", st)
        if len(regexp_list) > 0:
            min_occ = st.find(regexp_list[0])
            min_num = regexp_list[0]
            max_occ = len(st) - 1 - st[::-1].find(regexp_list[-1])
            max_num = regexp_list[-1]
        for k in NUMBER_NAMES.keys():
            res = [idx for idx in range(len(st)) if st.startswith(k, idx)]
            if len(res) > 0:
                if res[0] <= min_occ:
                    min_occ = res[0]
                    min_num = NUMBER_NAMES[k]
                if res[-1] >= max_occ:
                    max_occ = res[-1]
                    max_num = NUMBER_NAMES[k]
        counter += int(min_num + max_num)
    return counter


def part2v2(lines):
    NUMBER_NAMES = {
        "one": "o1e",
        "two": "t2o",
        "three": "t3e",
        "four": "f4r",
        "five": "f5e",
        "six": "s6x",
        "seven": "s7n",
        "eight": "e8t",
        "nine": "n9e",
    }
    int_list = []
    for idx, st in enumerate(lines):
        for k, v in NUMBER_NAMES.items():
            st = st.replace(k, v)
        lines[idx] = st

    for st in lines:
        int_list.append(re.findall(r"\d", st))
    counter = 0
    for num_list in int_list:
        counter += int(num_list[0] + num_list[-1])
    return counter


def part2v3(lines):
    NUMBER_NAMES = {
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9",
    }
    int_list = []
    counter = 0
    convert_to_int = lambda s: s if s.isdigit() else NUMBER_NAMES.get(s, s)
    for st in lines:
        int_list = re.findall(
            r"\d|" + "|".join(NUMBER_NAMES.keys()), st, overlapped=True
        )
        counter += int(convert_to_int(int_list[0]) + convert_to_int(int_list[-1]))
    return counter


if __name__ == "__main__":
    with advent.get_input() as file:
        lines = file.read().splitlines()

    print("############### Day 1 ###############")
    advent.submit_answer(1, part1(lines))
    # advent.submit_answer(2, part2(lines))
    # advent.submit_answer(2, part2v2(lines))
    advent.submit_answer(2, part2v3(lines))
