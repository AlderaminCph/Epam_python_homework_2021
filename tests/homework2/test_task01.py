import os

import pytest

from homework2.task1 import *


@pytest.mark.parametrize(
    ["file", "expected_result"],
    [
        (
            os.path.join("homework2/data.txt"),
            [
                "unmißverständliche",
                "Bevölkerungsabschub",
                "Kollektivschuldiger",
                "Werkstättenlandschaft",
                "Schicksalsfiguren",
                "politisch-strategischen",
                "Selbstverständlich",
                "Werkstättenlandschaft",
                "résistance-Bewegungen",
                "Zahlenverhältnis-",
            ],
        ),
    ],
)
def test_get_longest_diverse_words(file, expected_result: list):
    actual_result = get_longest_diverse_words(file)
    assert actual_result == expected_result
