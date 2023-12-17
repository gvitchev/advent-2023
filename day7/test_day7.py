from day7p2 import Hand, sort_hands
import pytest


@pytest.mark.parametrize(
    "hand, expected",
    [("T55J5", Hand.FOUR_OF_A_KIND), ("5JTQ3", Hand.PAIR), ("K276J", Hand.PAIR)],
)
def test_get_hand_type(hand, expected):
    assert expected.name == Hand.get_hand_type(hand)


@pytest.mark.parametrize(
    "hands, expected",
    [
        ([("KK677", 1), ("KTJJT", 5)], [("KTJJT", 5), ("KK677", 1)]),
    ],
)
def test_sort_hands(hands, expected):
    assert expected == sort_hands(hands)
