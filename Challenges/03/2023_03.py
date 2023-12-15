import re
import utils.advent as advent

advent.setup(2023, 3)


def find_symbols(lines):
    symbols = []
    for line in lines:
        symbols += re.findall(r"[^\d.\s]", line)
    return symbols


def check_left_pt2(lines, i, j):
    left = lines[i][max(j - 3, 0) : j]
    if not left[-1].isdigit():
        return []
    else:
        left_digit = left[-1]
        for c in left[::-1][1:]:
            if c.isdigit():
                left_digit = c + left_digit
            else:
                break
    return [int(left_digit)]


def check_right_pt2(lines, i, j):
    right = lines[i][j + 1 : min(j + 4, len(lines[i]))]
    if not right[0].isdigit():
        return []
    else:
        right_digit = right[0]
        for c in right[1:]:
            if c.isdigit():
                right_digit = right_digit + c
            else:
                break
    return [int(right_digit)]


def check_up_down_pt2(lines, i, j):
    upper = lines[i][max(j - 3, 0) : min(j + 4, len(lines[i]))]
    digits = re.findall(r"\d+", upper)
    if len(digits) == 0:
        return []
    elif len(digits) == 1:
        if upper[2].isdigit() or upper[3].isdigit() or upper[4].isdigit():
            return [int(digits[0])]
        else:
            return []
    else:
        if upper[2].isdigit() and upper[3].isdigit() and upper[4].isdigit():
            return [int(upper[2:5])]
        elif not upper[2].isdigit() and upper[3].isdigit() and not upper[4].isdigit():
            return [int(upper[3])]
        if upper[2].isdigit() and not upper[3].isdigit() and upper[4].isdigit():
            left_digit, right_digit = upper[2], upper[4]
            for i in range(len(upper[:2])):
                if upper[1 - i].isdigit():
                    left_digit = upper[1 - i] + left_digit
                else:
                    break
            for i in range(len(upper[5:])):
                if upper[5 + i].isdigit():
                    right_digit = right_digit + upper[5 + i]
                else:
                    break
            return [int(left_digit), int(right_digit)]

        left_digit = ""
        lft = 0
        if upper[2].isdigit() and not upper[4].isdigit():
            left_digit = upper[2]
            if upper[3].isdigit():
                left_digit = left_digit + upper[3]
            for c in upper[:2][::-1]:
                if c.isdigit():
                    left_digit = c + left_digit
                else:
                    break
            lft = int(left_digit)

        right_digit = ""
        rgt = 0
        if upper[4].isdigit() and not upper[2].isdigit():
            right_digit = upper[4]
            if upper[3].isdigit():
                right_digit = upper[3] + right_digit
            for c in upper[5:]:
                if c.isdigit():
                    right_digit = right_digit + c
                else:
                    break
            rgt = int(right_digit)
        if lft == 0 and rgt == 0:
            return []
        if lft == 0:
            return [rgt]
        elif rgt == 0:
            return [lft]
        else:
            return [lft, rgt]


def check_left(lines, i, j):
    left = lines[i][max(j - 3, 0) : j]
    if not left[-1].isdigit():
        return 0
    else:
        left_digit = left[-1]
        for c in left[::-1][1:]:
            if c.isdigit():
                left_digit = c + left_digit
            else:
                break
    return int(left_digit)


def check_right(lines, i, j):
    right = lines[i][j + 1 : min(j + 4, len(lines[i]))]
    if not right[0].isdigit():
        return 0
    else:
        right_digit = right[0]
        for c in right[1:]:
            if c.isdigit():
                right_digit = right_digit + c
            else:
                break
    return int(right_digit)


def check_up_down(lines, i, j):
    upper = lines[i][max(j - 3, 0) : min(j + 4, len(lines[i]))]
    digits = re.findall(r"\d+", upper)
    if len(digits) == 0:
        return 0
    elif len(digits) == 1:
        if upper[2].isdigit() or upper[3].isdigit() or upper[4].isdigit():
            return int(digits[0])
        else:
            return 0
    else:
        if upper[2].isdigit() and upper[3].isdigit() and upper[4].isdigit():
            return int(upper[2:5])
        elif not upper[2].isdigit() and upper[3].isdigit() and not upper[4].isdigit():
            return int(upper[3])
        if upper[2].isdigit() and not upper[3].isdigit() and upper[4].isdigit():
            left_digit, right_digit = upper[2], upper[4]
            for i in range(len(upper[:2])):
                if upper[1 - i].isdigit():
                    left_digit = upper[1 - i] + left_digit
                else:
                    break
            for i in range(len(upper[5:])):
                if upper[5 + i].isdigit():
                    right_digit = right_digit + upper[5 + i]
                else:
                    break
            return int(left_digit) + int(right_digit)

        left_digit = ""
        lft = 0
        if upper[2].isdigit() and not upper[4].isdigit():
            left_digit = upper[2]
            if upper[3].isdigit():
                left_digit = left_digit + upper[3]
            for c in upper[:2][::-1]:
                if c.isdigit():
                    left_digit = c + left_digit
                else:
                    break
            lft = int(left_digit)

        right_digit = ""
        rgt = 0
        if upper[4].isdigit() and not upper[2].isdigit():
            right_digit = upper[4]
            if upper[3].isdigit():
                right_digit = upper[3] + right_digit
            for c in upper[5:]:
                if c.isdigit():
                    right_digit = right_digit + c
                else:
                    break
            rgt = int(right_digit)
        return lft + rgt


def part1(lines):
    counter = 0
    for i in range(len(lines)):
        for j in range(len(lines[i])):
            if not lines[i][j].isdigit() and lines[i][j] != ".":
                if i > 0:
                    counter += check_up_down(lines, i - 1, j)
                counter += check_left(lines, i, j)
                counter += check_right(lines, i, j)
                if i < len(lines) - 1:
                    counter += check_up_down(lines, i + 1, j)
    return counter


def part2(lines):
    counter = 0
    for i in range(len(lines)):
        for j in range(len(lines[i])):
            if lines[i][j] == "*":
                digits = []
                if i > 0:
                    digits += check_up_down_pt2(lines, i - 1, j)
                digits += check_left_pt2(lines, i, j)
                digits += check_right_pt2(lines, i, j)
                if i < len(lines) - 1:
                    digits += check_up_down_pt2(lines, i + 1, j)
                if len(digits) == 2:
                    counter += digits[0] * digits[1]
    return counter


if __name__ == "__main__":
    with advent.get_input() as file:
        lines = file.read().splitlines()

    print("############### Day 3 ###############")
    advent.submit_answer(1, part1(lines))
    advent.submit_answer(2, part2(lines))
