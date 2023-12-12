from day5p2 import find_ranges_for_single_range
import pytest


@pytest.mark.parametrize(
    "range, mappings, expected",
    [
        ((100, 50), [(200, 50, 100)], [(250, 50)]),
        ((100, 50), [(200, 100, 50)], [(200, 50)]),
        ((100, 50), [(200, 150, 50)], [(100, 50)]),
        ((100, 50), [(200, 100, 25)], [(200, 25), (125, 25)]),
    ],
)
def test_find_ranges_for_single_range(range, mappings, expected):
    assert expected == find_ranges_for_single_range(range, mappings)
