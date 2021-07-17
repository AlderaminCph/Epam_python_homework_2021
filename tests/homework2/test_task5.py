import string

import pytest

from homework2.task5 import my_range_function


@pytest.mark.parametrize(
    ["iterable_values", "arguments", "expected_result"],
    [
        (string.ascii_lowercase, "g", ["a", "b", "c", "d", "e", "f"]),
        (
            string.ascii_lowercase,
            ("g", "p"),
            ["g", "h", "i", "j", "k", "l", "m", "n", "o"],
        ),
        (string.ascii_lowercase, ("p", "g", -2), ["p", "n", "l", "j", "h"]),
        ([1, 2, 3, 4, 5], (2, 5), [2, 3, 4]),
    ],
)
def test_my_range_function(iterable_values, arguments, expected_result):
    our_result = my_range_function(iterable_values, *arguments)
    assert our_result == expected_result


def test_my_range_function_zero_step():
    with pytest.raises(ValueError):
        my_range_function(string.ascii_lowercase, "g", "p", 0)


def test_my_range_beyond_limits():
    with pytest.raises(ValueError):
        my_range_function([1, 2, 3, 4, 5], (1, 6, 1))
