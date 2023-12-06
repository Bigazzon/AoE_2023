import re
import utils.advent as advent

advent.setup(2023, 2)


def parse_string(line):
    game_id = int(re.findall(r"\d+", line)[0])
    sets = line.split(":")[-1].split(";")
    parsed_sets = []
    for s in sets:
        s = s.strip()
        game_data = s.split(",")
        game_dict = {"red": 0, "green": 0, "blue": 0}
        for data in game_data:
            data = data.strip()
            number, color = data.split(" ")
            game_dict[color] = int(number)
        parsed_sets.append(game_dict)
    return game_id, parsed_sets


def check_game(game_id, game, rgb):
    for st in game:
        for color in st.keys():
            if st[color] > rgb[color]:
                return 0
    return game_id


def check_minimum(game):
    rgb = {name: 0 for name in ["red", "green", "blue"]}
    for st in game:
        for color in st.keys():
            if st[color] > rgb[color]:
                rgb[color] = st[color]
    return rgb["red"] * rgb["green"] * rgb["blue"]


def part1(lines, rgb):
    rgb = {name: color for name, color in zip(["red", "green", "blue"], rgb)}
    counter = 0
    for s in lines:
        id, game_info = parse_string(s)
        counter += check_game(id, game_info, rgb)
    return counter


def part2(lines):
    counter = 0
    for s in lines:
        _, game_info = parse_string(s)
        counter += check_minimum(game_info)
    return counter


if __name__ == "__main__":
    with advent.get_input() as file:
        lines = file.read().splitlines()

    print("############### Day 2 ###############")
    advent.submit_answer(1, part1(lines, rgb=[12, 13, 14]))
    advent.submit_answer(2, part2(lines))
