import utils.advent as advent

advent.setup(2023, 15)


def parse_input(lines):
    input = lines.split(",")
    new_input = []
    for inp in input:
        new_input.append([ord(c) for c in inp])
    return new_input


def parse_input_pt2(lines):
    input = lines.split(",")
    new_input = []
    for inp in input:
        label = inp.split("=")[0].split("-")[0]
        sign = inp[len(label)]
        try:
            num = int(inp[len(label) + 1])
        except:
            num = None
        new_input.append([[ord(c) for c in label], label, sign, num])
    return new_input


def compute_hash(l):
    count = 0
    for num in l:
        count += num
        count *= 17
        count %= 256
    return count


def count_box(index, box):
    count = 0
    for idx, num in enumerate(box):
        count += (index + 1) * (idx + 1) * num
    return count


def part1(lines):
    input = parse_input(lines)

    counter = 0

    for inp in input:
        counter += compute_hash(inp)

    return counter


def part2(lines):
    input = parse_input_pt2(lines)
    boxes = {i: [[], []] for i in range(256)}

    for inp in input:
        box_label = compute_hash(inp[0])

        if inp[2] == "=":
            if inp[1] in boxes[box_label][0]:
                ind = boxes[box_label][0].index(inp[1])
                boxes[box_label][1][ind] = inp[3]
            else:
                boxes[box_label][0].append(inp[1])
                boxes[box_label][1].append(inp[3])
        elif inp[2] == "-":
            if inp[1] in boxes[box_label][0]:
                ind = boxes[box_label][0].index(inp[1])
                del boxes[box_label][0][ind]
                del boxes[box_label][1][ind]
        else:
            raise Exception("Unknown sign")

    counter = 0
    for i, b in enumerate(boxes.values()):
        if len(b[1]) == 0:
            continue
        counter += count_box(i, b[1])

    return counter


if __name__ == "__main__":
    # with open("15/2023_15_debug.txt", "r") as file:
    #     lines = file.read().splitlines()[0]
    with advent.get_input() as file:
        lines = file.read().splitlines()[0]

    print("############### Day 15 ###############")
    advent.submit_answer(1, part1(lines))
    advent.submit_answer(2, part2(lines))
