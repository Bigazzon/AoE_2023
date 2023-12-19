import re
import utils.advent as advent

advent.setup(2023, 19)


def parse_input(lines):
    workflows = {}
    i = 0
    while True:
        if lines[i] == "":
            break
        new_l = lines[i].replace("}", "").split("{")
        conds = new_l[1].split(",")
        workflows[new_l[0]] = conds
        i += 1
    parts = []
    for j in range(i + 1, len(lines)):
        components = lines[j].replace("{", "").replace("}", "").split(",")
        comp_dict = {}
        for c in components:
            k, v = c.split("=")
            comp_dict[k] = int(v)
        parts.append(comp_dict)
    return workflows, parts


def check_final_state(c, p, accepted, rejected):
    if c == "A":
        accepted.append(p)
    elif c == "R":
        rejected.append(p)
    else:
        raise Exception("Invalid final state")
    return accepted, rejected


def count_final_output_pt1(accepted):
    counter = 0
    for a in accepted:
        for v in a.values():
            counter += v
    return counter


def count_final_output_pt2(accepted):
    counter = 0
    for a in accepted:
        count = 1
        for v in a.values():
            count *= v[1] - v[0] + 1
        counter += count
    return counter


def compute_ranges(state, label, step, components):
    condition, new_label = state.split(":")
    old_range = components[condition[0]]
    value = int(re.findall(r"\d+", condition)[0])

    if "<" in condition:
        if old_range[0] < value:
            pos_range = [old_range[0], value - 1]
            neg_range = [value, old_range[1]]
    elif ">" in condition:
        if old_range[1] > value:
            pos_range = [value + 1, old_range[1]]
            neg_range = [old_range[0], value]
    else:
        raise Exception("Invalid condition")

    pos_dict = components.copy()
    pos_dict[condition[0]] = pos_range
    pos = [new_label, 0, pos_dict]

    neg_dict = components.copy()
    neg_dict[condition[0]] = neg_range
    neg = [label, step + 1, neg_dict]
    return pos, neg


def part1(lines):
    workflows, parts = parse_input(lines)

    accepted = []
    rejected = []

    for index, part in enumerate(parts):
        workflow_label = "in"
        x, m, a, s = part["x"], part["m"], part["a"], part["s"]

        while (len(accepted) + len(rejected)) <= index:
            workflow = workflows[workflow_label].copy()

            while workflow:
                current_state = workflow.pop(0)

                if len(current_state) == 1:
                    accepted, rejected = check_final_state(
                        current_state, part, accepted, rejected
                    )
                    break

                if not workflow:
                    workflow_label = current_state
                    break

                condition, new_workflow_label = current_state.split(":")
                condition_evaluated = eval(condition)

                if condition_evaluated:
                    if len(new_workflow_label) == 1:
                        accepted, rejected = check_final_state(
                            new_workflow_label, part, accepted, rejected
                        )
                        break
                    workflow_label = new_workflow_label
                    break

    return count_final_output_pt1(accepted)


def part2(lines):
    workflows, _ = parse_input(lines)

    min, max = 1, 4000
    accepted = []

    q = [
        ["in", 0, {"x": [min, max], "m": [min, max], "a": [min, max], "s": [min, max]}]
    ]
    while q:
        workflow_label, step, components = q.pop(0)

        if workflow_label == "A":
            accepted.append(components)
            continue
        elif workflow_label == "R":
            continue

        workflow = workflows[workflow_label].copy()
        current_state = workflow[step]

        if ":" not in current_state:
            q.append([current_state, 0, components])
            continue

        pos, neg = compute_ranges(current_state, workflow_label, step, components)
        q.append(pos)
        q.append(neg)

    return count_final_output_pt2(accepted)


if __name__ == "__main__":
    # with open("challenges/19/2023_19_debug.txt", "r") as file:
    #     lines = file.read().splitlines()
    with advent.get_input() as file:
        lines = file.read().splitlines()

    print("############### Day 19 ###############")
    advent.submit_answer(1, part1(lines))
    advent.submit_answer(2, part2(lines))
