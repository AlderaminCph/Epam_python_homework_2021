import pytest

from homework1.task04 import check_sum_of_four


@pytest.mark.parametrize(
    ["a", "b", "c", "d", "expected_result"],
    [
        ([1, 2], [-2, -1], [-1, 2], [0, 2], 2),
        ([1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], 0),
    ],
)
def test_check_sum_of_four(a: list, b: list, c: list, d: list, expected_result: int):
    our_result = check_sum_of_four(a, b, c, d)

    assert our_result == expected_result
