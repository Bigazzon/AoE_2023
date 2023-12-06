import utils.advent as advent

advent.setup(2023, 5)

MAPS = [
    "seeds",
    "seed-to-soil",
    "soil-to-fertilizer",
    "fertilizer-to-water",
    "water-to-light",
    "light-to-temperature",
    "temperature-to-humidity",
    "humidity-to-location",
]


def parse_input(lines):
    mapping_dict = {k: [] for k in MAPS}
    mapping_index = 0
    for l in lines:
        if "seeds:" in l:
            mapping_dict["seeds"] = [
                int(l) for l in l.split(":")[-1].split(" ") if l != ""
            ]
            continue
        elif l == "":
            mapping_index += 1
            continue
        elif MAPS[mapping_index] in l:
            continue
        range_values = [int(n) for n in l.split(" ")]
        mapping_dict[MAPS[mapping_index]].append(range_values)
    return mapping_dict


def part1(lines):
    mapping_dict = parse_input(lines)
    location_list = []
    for seed in mapping_dict["seeds"]:
        source = int(seed)
        target = source
        for k in mapping_dict.keys():
            if k == "seeds":
                continue
            for mapping in mapping_dict[k]:
                if mapping[1] <= source < mapping[1] + mapping[-1]:
                    target = mapping[0] + source - mapping[1]
                    source = target
                    break
        location_list.append(target)
    return min(location_list)


def part2(lines):
    mapping_dict = parse_input(lines)
    mapping_dict["seeds"] = [
        mapping_dict["seeds"][2 * i : 2 * i + 2]
        for i in range(len(mapping_dict["seeds"]) // 2)
    ]
    location_list = []
    source_check_list = mapping_dict["seeds"]

    for k in mapping_dict.keys():
        if k == "seeds":
            continue

        target_check_list = []
        while len(source_check_list) > 0:
            start_source, source_length = source_check_list.pop(0)
            found = False
            for mapping in mapping_dict[k]:
                mapping_start_target, mapping_start_source, mapping_length = mapping
                if (
                    mapping_start_source
                    <= start_source
                    < mapping_start_source + mapping_length
                ):
                    found = True
                    start_target = (
                        mapping_start_target + start_source - mapping_start_source
                    )
                    if (
                        start_source + source_length
                        < mapping_start_source + mapping_length
                    ):
                        target_length = source_length
                        target_check_list.append([start_target, target_length])
                    else:
                        target_length = (
                            mapping_start_source + mapping_length - start_source
                        )
                        target_check_list.append([start_target, target_length])

                        source_check_list.append(
                            [
                                mapping_start_source + mapping_length,
                                (start_source + source_length)
                                - (mapping_start_source + mapping_length),
                            ]
                        )
                    break

            if not found:
                target_check_list.append([start_source, source_length])

        source_check_list = target_check_list

    return min([t[0] for t in target_check_list])


if __name__ == "__main__":
    # with open("05/2023_05_debug.txt", "r") as file:
    #     lines = file.read().splitlines()
    with advent.get_input() as file:
        lines = file.read().splitlines()

    print("############### Day 5 ###############")
    advent.submit_answer(1, part1(lines))
    advent.submit_answer(2, part2(lines))
