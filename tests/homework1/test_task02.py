import pytest

from homework1.task02 import check_fibonacci


@pytest.mark.parametrize(
    ["value", "expected_result"],
    [
        (
            (
                0,
                1,
                1,
                2,
                3,
                5,
                8,
                13,
                21,
                34,
                55,
                89,
                144,
                233,
                377,
                610,
                987,
                1597,
                2584,
                4181,
                6765,
            ),
            True,
        ),
        ((1, 2, 3, 4, 5), False),
        ((55, 89, 144, 233, 377, 610), True),
        ((8, 13, 21), True),
        ((0, 0, 0, 0, 0), False),
        ((2, 1, 3, 4, 7), False),
        ((5, 6, 17, 11, 28), False),
    ],
)
def test_check_fibonacci(value: int, expected_result: bool):
    actual_result = check_fibonacci(value)

    assert actual_result == expected_result
