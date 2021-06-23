import os
from typing import Tuple

import pytest

from homework1.task03 import find_maximum_and_minimum


@pytest.mark.parametrize(
    ["input_file", "expected_result"],
    [
        (os.path.join("tests/homework1/input_files", "input1.txt"), (0, 12)),
        (os.path.join("tests/homework1/input_files", "input2.txt"), (-22, 100)),
        (os.path.join("tests/homework1/input_files", "input3.txt"), (0, 0)),
        (os.path.join("tests/homework1/input_files", "input4.txt"), (-1, 812)),
        (os.path.join("tests/homework1/input_files", "input5.txt"), (-400, -1)),
    ],
)
def test_find_maximum_and_minimum(input_file: str, expected_result: Tuple[int, int]):
    our_result = find_maximum_and_minimum(input_file)

    assert our_result == expected_result
