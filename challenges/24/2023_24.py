import utils.advent as advent
import sympy

advent.setup(2023, 24)


def parse_input(lines):
    new_lines = []
    for l in lines:
        pos, vel = l.split("@")
        new_lines.append(
            ([int(x) for x in pos.split(",")], [int(x) for x in vel.split(",")])
        )
    return new_lines


def line_equation_2d(point, direction):
    x, y = point
    vx, vy = direction
    return x, y, vx, vy


def line_equation_3d(point, direction):
    x, y, z = point
    vx, vy, vz = direction
    return x, y, z, vx, vy, vz


def test_coords_2d(coord, x, y):
    if coord is None:
        return False
    x1, x2 = x
    y1, y2 = y
    return x1 <= coord[0] <= x2 and y1 <= coord[1] <= y2


def intersection_2d(line1, line2):
    x1, y1, vx1, vy1 = line1
    x2, y2, vx2, vy2 = line2

    determinant = vx1 * vy2 - vy1 * vx2
    if determinant == 0:
        return None

    t = ((x2 - x1) * vy2 - (y2 - y1) * vx2) / determinant
    s = ((x2 - x1) * vy1 - (y2 - y1) * vx1) / determinant

    if t > 0 and s > 0:
        intersection_x = x1 + t * vx1
        intersection_y = y1 + t * vy1
        return intersection_x, intersection_y
    else:
        return None


def part1(lines, x=[7, 27], y=[7, 27]):
    hailstones = parse_input(lines)

    lines = []
    for h in hailstones:
        equation = line_equation_2d(h[0][:2], h[1][:2])
        lines.append(equation)

    intersection_coords = []
    count = 0
    for idx in range(len(hailstones)):
        for ivx2 in range(1, len(hailstones[idx:])):
            intersection = intersection_2d(lines[idx], lines[idx + ivx2])
            intersection_coords.append(intersection)

            if test_coords_2d(intersection, x, y):
                count += 1

    return count


def part2(lines):
    hailstones = parse_input(lines)

    lines = []
    for h in hailstones:
        equation = line_equation_3d(h[0], h[1])
        lines.append(equation)

    equations = []
    sx, sy, sz, svx, svy, svz = sympy.symbols("sx, sy, sz, svx, svy, svz")
    for i, (x, y, z, vx, vy, vz) in enumerate(lines[:3]):
        equations.append((sx - x) * (vy - svy) - (sy - y) * (vx - svx))
        equations.append((sy - y) * (vz - svz) - (sz - z) * (vy - svy))
    answers = sympy.solve(equations)
    answer = [
        soln
        for soln in answers
        if soln[sx] % 1 == 0 and soln[sy] % 1 == 0 and soln[sz] % 1 == 0
    ][0]
    return answer[sx] + answer[sy] + answer[sz]


if __name__ == "__main__":
    # with open("challenges/24/2023_24_debug.txt", "r") as file:
    #     lines = file.read().splitlines()
    with advent.get_input() as file:
        lines = file.read().splitlines()

    print("############### Day 24 ###############")
    advent.submit_answer(
        1,
        part1(
            lines,
            x=[200000000000000, 400000000000000],
            y=[200000000000000, 400000000000000],
        ),
    )
    advent.submit_answer(2, part2(lines))
