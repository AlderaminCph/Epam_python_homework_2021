import os

import pytest
from homework2.task1 import *


@pytest.mark.parametrize(
    ["file", "expected_result"],
    [
        (
            os.path.join("homework2/data.txt"),
            [
                "unmißverständlich",
                "unmißverständliche",
                "Bevölkerungsabsch",
                "Bevölkerungsabschu",
                "Bevölkerungsabschub",
                "Kollektivschuldiger",
                "Selbstverständlich",
                "Kollektivschuldig",
                "Kollektivschuldige",
                "Werkstättenlandschaf",
            ],
        ),
    ],
)
def test_get_longest_diverse_words(file, expected_result: list):
    our_result = get_longest_diverse_words(file)
    assert our_result == expected_result
