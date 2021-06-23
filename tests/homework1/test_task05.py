import pytest

from homework1.task05 import find_maximal_subarray_sum


@pytest.mark.parametrize(
    ["nums", "k", "expected_result"],
    [
        ([1, 3, -1, -3, 5, 3, 6, 7], 3, 16),
        ([3,2,5,4,1],2,9),
        ([-2, -5, 6, -2, -3, 1, 5, -6],5,7)
    ],
)
def test_find_maximal_subarray_sum(nums: list, k: int, expected_result: int):
    our_result = find_maximal_subarray_sum(nums, k)

    assert our_result == expected_result
