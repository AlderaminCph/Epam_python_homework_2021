import pytest

from homework3.task4 import is_armstrong


@pytest.mark.parametrize(
    ["number", "expected_result"],
    [
        (9, True),
        (10, False),
        (153, True),
        (0, True),
    ],
)
def test_is_armstrong(number, expected_result):
    our_result = is_armstrong(number)
    assert our_result == expected_result
