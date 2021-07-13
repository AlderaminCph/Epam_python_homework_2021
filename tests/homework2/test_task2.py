import pytest

from homework2.task2 import major_and_minor_elem


@pytest.mark.parametrize(
    ["input_list", "expected_result"],
    [
        ([3, 2, 3], (3, 2)),
        ([2, 2, 1, 1, 1, 2, 2], (2, 1)),
        ([0], (0, 0)),
        ([1, 1, 1, 1, 1, 1], (1, 1)),
    ],
)
def test_major_and_minor_elem(input_list, expected_result: list):
    our_result = major_and_minor_elem(input_list)
    assert our_result == expected_result


def test_major_and_minor_elem_empty_list():
    with pytest.raises(ValueError):
        major_and_minor_elem([])
