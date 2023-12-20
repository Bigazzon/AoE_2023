import math
import re

import tqdm
import utils.advent as advent

advent.setup(2023, 20)

# % flip-flop: on-off state, low pulse switches state and sends a corresponding (off->low/on->high) pulse
# & conjunction: remember state of last pulse of each input, if all inputs are high sends low, else sends high
# broadcaster: forwards pulses from input to all outputs
# button: sends a low pulse to broadcaster


def parse_input(lines):
    modules_dict = {}
    conjuction_names = []
    for line in lines:
        if line.startswith("broadcaster"):
            modules_dict["broadcaster"] = {"type": "broadcaster", "output": []}
            l = line.split(" -> ")[-1].replace(" ", "").split(",")
            for m in l:
                modules_dict["broadcaster"]["output"].append(m)
        elif line.startswith("%"):
            module_name = re.findall(r"(\w+)", line.replace("%", ""))[0]
            modules_dict[module_name] = {"type": "flip-flop", "state": 0, "output": []}
            l = line.split(" -> ")[-1].replace(" ", "").split(",")
            for m in l:
                modules_dict[module_name]["output"].append(m)
        elif line.startswith("&"):
            module_name = re.findall(r"(\w+)", line.replace("%", ""))[0]
            conjuction_names.append(module_name)
            modules_dict[module_name] = {
                "type": "conjunction",
                "input": {},
                "output": [],
            }
            l = line.split(" -> ")[-1].replace(" ", "").split(",")
            for m in l:
                modules_dict[module_name]["output"].append(m)

    for line in lines:
        l = line.split(" -> ")[-1].replace(" ", "").split(",")
        for m in l:
            if m in conjuction_names:
                modules_dict[m]["input"][
                    line.split(" -> ")[0].replace("%", "").replace("&", "")
                ] = 0

    return modules_dict


def compute_pulse(modules_list, pulse):
    input_module_name = pulse[1]
    if input_module_name not in modules_list:
        return [], modules_list
    input_module = modules_list[input_module_name]
    level = pulse[0]
    add_pulses = []
    outputs = []
    if input_module["type"] == "broadcaster":
        for m in input_module["output"]:
            pulse = level
            add_pulses.append([pulse, m])
            outputs.append(m)
    elif input_module["type"] == "flip-flop":
        if level == 0:
            input_module["state"] = 1 - input_module["state"]
            pulse = input_module["state"]
            for m in input_module["output"]:
                add_pulses.append([pulse, m])
                outputs.append(m)
    elif input_module["type"] == "conjunction":
        pulse = 0 if all(input_module["input"].values()) else 1
        for m in input_module["output"]:
            add_pulses.append([pulse, m])
            outputs.append(m)
    else:
        raise ValueError("Unknown module type")

    for m in outputs:
        if m in modules_list and modules_list[m]["type"] == "conjunction":
            modules_list[m]["input"][input_module_name] = pulse
    return add_pulses, modules_list


def find_parents(lines, name):
    parents = []
    for line in lines:
        symbol = "%" if line.startswith("%") else "&"
        module_name = re.findall(r"(\w+)", line.replace("%", "").replace("&", ""))[0]
        l = line.split(" -> ")[-1].replace(" ", "").split(",")
        for m in l:
            if m == name.replace("%", "").replace("&", ""):
                parents.append(symbol + module_name)
    return parents


def lcm(a):
    res = 1
    for num in a:
        num = num[0]
        res = (num * res) // math.gcd(num, res)
    return res


def part1(lines):
    modules = parse_input(lines)

    low_count, high_count = 0, 0
    for _ in range(1000):
        q = [[0, "broadcaster"]]
        while q:
            pulse = q.pop(0)
            additional_pulses, modules = compute_pulse(modules, pulse)
            if pulse[0] == 0:
                low_count += 1
            else:
                high_count += 1
            q.extend(additional_pulses)

    return low_count * high_count


def part2(lines):
    modules = parse_input(lines)
    parents = {}
    lvl = 0
    parents[0] = ["rx"]

    while len(parents[lvl]) == 1:
        lvl += 1
        parents[lvl] = find_parents(lines, parents[lvl - 1][0])

    count = 0
    names = parents[lvl]
    cycles_len = [[] for _ in range(len(names))]
    found_cycle = [False for _ in range(len(names))]

    with tqdm.tqdm(total=1000000000) as pbar:
        while not all(found_cycle):
            count += 1
            q = [[0, "broadcaster"]]
            while q:
                pulse = q.pop(0)
                additional_pulses, modules = compute_pulse(modules, pulse)
                q.extend(additional_pulses)

                par = modules[parents[1][0].replace("&", "")]["input"]
                if pulse[1] == "rx":
                    for i, p in enumerate(par.values()):
                        if p == 1 and count not in cycles_len[i]:
                            cycles_len[i].append(count)
                            if (
                                len(cycles_len[i]) > 1
                                and (cycles_len[i][-1] - cycles_len[i][-2])
                                == cycles_len[i][0]
                            ):
                                found_cycle[i] = True
            pbar.update(1)

    tot = lcm(cycles_len)
    return tot


if __name__ == "__main__":
    # with open("challenges/20/2023_20_debug_b.txt", "r") as file:
    #     lines = file.read().splitlines()
    with advent.get_input() as file:
        lines = file.read().splitlines()

    print("############### Day 20 ###############")
    advent.submit_answer(1, part1(lines))
    advent.submit_answer(2, part2(lines))
