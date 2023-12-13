import utils.advent as advent

advent.setup(2023, 13)


def parse_input(lines):
    blocks = [[]]
    i = 0
    for l in lines:
        if l == "":
            i += 1
            blocks.append([])
            continue
        blocks[i].append(l)
    return blocks


def transpose(b):
    transpose_b = ["" for _ in range(len(b[0]))]
    for i in range(len(b)):
        for j in range(len(b[i])):
            transpose_b[j] += b[i][j]
    return transpose_b


def check_reflections(b):
    reflection_indices = []

    for i in range(1, len(b)):
        ok = True
        for j in range(1, min(i + 1, len(b) - i + 1)):
            for l in range(len(b[0])):
                if b[i - j][l] != b[i + j - 1][l]:
                    ok = False
                    break
            if not ok:
                break
        if not ok:
            continue
        reflection_indices.append(i)
    return reflection_indices


def check_reflections_w_error(b):
    reflection_indices = []
    for i in range(1, len(b)):
        errors = 0
        ok = True
        for j in range(1, min(i + 1, len(b) - i + 1)):
            for l in range(len(b[0])):
                if b[i - j][l] != b[i + j - 1][l]:
                    errors += 1
                    if errors > 1:
                        ok = False
                        break
            if not ok:
                break
        if not ok:
            continue
        if errors == 1:
            reflection_indices.append(i)
    return reflection_indices


def part1(lines):
    blocks = parse_input(lines)
    counter = 0

    for b in blocks:
        # extract row indeces
        rows = check_reflections(b)

        # extract column indeces
        cols = check_reflections(transpose(b))

        counter += sum(cols) + sum(rows) * 100

    return counter


def part2(lines):
    blocks = parse_input(lines)
    counter = 0

    for b in blocks:
        # extract row indeces
        rows = check_reflections_w_error(b)

        # extract column indeces
        cols = check_reflections_w_error(transpose(b))

        counter += sum(cols) + sum(rows) * 100

    return counter


if __name__ == "__main__":
    # with open("13/2023_13_debug.txt", "r") as file:
    #     lines = file.read().splitlines()
    with advent.get_input() as file:
        lines = file.read().splitlines()

    print("############### Day 13 ###############")
    advent.submit_answer(1, part1(lines))
    advent.submit_answer(2, part2(lines))
