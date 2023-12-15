import utils.advent as advent
from collections import Counter

advent.setup(2023, 7)

REPLACE_CARD = {
    "A": "A",
    "K": "B",
    "Q": "C",
    "J": "D",
    "T": "E",
    "9": "F",
    "8": "G",
    "7": "H",
    "6": "I",
    "5": "J",
    "4": "K",
    "3": "L",
    "2": "M",
}
REPLACE_CARD_PT2 = {
    "A": "A",
    "K": "B",
    "Q": "C",
    "T": "E",
    "9": "F",
    "8": "G",
    "7": "H",
    "6": "I",
    "5": "J",
    "4": "K",
    "3": "L",
    "2": "M",
    "J": "N",
}

STRENGTH_ORDER = ["5", "4", "32", "3", "22", "2", ""]


def parse_input(lines):
    hands, bids = [], []
    for l in lines:
        hand, bid = l.split(" ")
        hands.append(hand)
        bids.append(bid)
    return hands, bids


def part1(lines):
    hands, bids = parse_input(lines)
    ordered_hands = {s: {} for s in STRENGTH_ORDER}
    for hand, bid in zip(hands, bids):
        count = Counter(hand)
        strength = "".join(
            [str(c) for c in sorted(list(count.values()), reverse=True) if c > 1]
        )

        ordered_hands[strength]["".join([REPLACE_CARD[c] for c in hand])] = bid

    ordered_bids = []
    for o in STRENGTH_ORDER:
        ordered_bids += list(dict(sorted(ordered_hands[o].items())).values())
    reversed_bids = ordered_bids[::-1]
    return sum([int(bid) * (idx + 1) for idx, bid in enumerate(reversed_bids)])


def part2(lines):
    hands, bids = parse_input(lines)
    ordered_hands = {s: {} for s in STRENGTH_ORDER}
    for hand, bid in zip(hands, bids):
        count = Counter(hand)
        add_j = count["J"] if "J" in count.keys() else 0
        del count["J"]
        strength = [str(c) for c in sorted(list(count.values()), reverse=True) if c > 1]
        if add_j > 0:
            if len(strength) == 0:
                strength = [str(min(add_j + 1, 5))]
            else:
                strength[0] = str(int(strength[0]) + add_j)
            if add_j > 1 and add_j in strength:
                strength.remove(str(add_j))
        strength = "".join([str(s) for s in strength])
        ordered_hands[strength]["".join([REPLACE_CARD_PT2[c] for c in hand])] = bid
    ordered_bids = []
    for o in STRENGTH_ORDER:
        ordered_bids += list(dict(sorted(ordered_hands[o].items())).values())
    reversed_bids = ordered_bids[::-1]
    return sum([int(bid) * (idx + 1) for idx, bid in enumerate(reversed_bids)])


if __name__ == "__main__":
    # with open("Challenges/07/2023_07_debug.txt", "r") as file:
    #     lines = file.read().splitlines()
    with advent.get_input() as file:
        lines = file.read().splitlines()

    print("############### Day 7 ###############")
    advent.submit_answer(1, part1(lines))
    advent.submit_answer(2, part2(lines))
