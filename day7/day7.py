import re
from enum import Enum

ORDERED_CARDS = ["2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K", "A"]


class Hand(Enum):
    HIGH_CARD = 1
    PAIR = 2
    TWO_PAIR = 3
    THREE_OF_A_KIND = 4
    FULL_HOUSE = 5
    FOUR_OF_A_KIND = 6
    FIVE_OF_A_KIND = 7

    def get_hand_type(hand):
        shand = sorted(hand)
        last_char = shand[0]
        same_cards = []
        same_of_current_char = 1
        for c in shand[1:]:
            if c == last_char:
                same_of_current_char += 1
            elif same_of_current_char > 1:
                same_cards.append(same_of_current_char)
                last_char = c
                same_of_current_char = 1
            else:
                last_char = c
        if same_of_current_char > 1:
            same_cards.append(same_of_current_char)

        same_cards.sort()
        if same_cards == [5]:
            return Hand.FIVE_OF_A_KIND.name
        elif same_cards == [4]:
            return Hand.FOUR_OF_A_KIND.name
        elif same_cards == [2, 3]:
            return Hand.FULL_HOUSE.name
        elif same_cards == [3]:
            return Hand.THREE_OF_A_KIND.name
        elif same_cards == [2, 2]:
            return Hand.TWO_PAIR.name
        elif same_cards == [2]:
            return Hand.PAIR.name
        else:
            return Hand.HIGH_CARD.name


def sort_hands(hands):
    if len(hands) == 0:
        return hands
    initial_dict = {}
    for card in ORDERED_CARDS:
        initial_dict[card] = []
    for hand in hands:
        initial_dict[hand[0][len(hand[0]) - 1]].append(hand)
    for i in range(len(hands[0][0]) - 1):
        new_dict = {}
        for card in ORDERED_CARDS:
            new_dict[card] = []
        for card in ORDERED_CARDS:
            for hand in initial_dict[card]:
                new_dict[hand[0][len(hand[0]) - 2 - i]].append(hand)
        initial_dict = new_dict
    result = []
    for card in ORDERED_CARDS:
        for hand in initial_dict[card]:
            result.append(hand)
    return result


def solve(hands):
    hands_by_type = dict([(x.name, []) for x in list(Hand)])
    for h in hands:
        split = re.split(r"\s+", h)
        hand = (split[0], int(split[1]))
        hands_by_type[Hand.get_hand_type(hand[0])].append(hand)

    total = 0
    idx = 1
    for hand_type in list(Hand):
        hands = hands_by_type[hand_type.name]
        s = sort_hands(hands)
        for hand in s:
            total += hand[1] * idx
            idx += 1
    print(total)


sample = """32T3K 765
T55J5 684
KK677 28
KTJJT 220
QQQJA 483"""

if __name__ == "__main__":
    solve(sample.split("\n"))

    input = []
    with open("input.txt", "r") as f:
        for line in f:
            input.append(line)
    solve(input)
