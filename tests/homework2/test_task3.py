import pytest

from homework2.task3 import combinations


@pytest.mark.parametrize(
    ["input_lists", "expected_lists"],
    [
        ([[1, 2], [3, 4]], [[1, 3], [1, 4], [2, 3], [2, 4]]),
    ],
)
def test_combinations(input_lists, expected_lists):
    our_result = combinations(*input_lists)
    assert our_result == expected_lists


def test_combinations_empty_list():
    with pytest.raises(ValueError):
        combinations([])
