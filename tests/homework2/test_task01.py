import os

import pytest

from homework2.task1 import *

file = "homework2/data.txt"


@pytest.mark.parametrize(
    ["inputfile", "expected_result"],
    [
        (
            os.path.join(file),
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
def test_get_longest_diverse_words(inputfile, expected_result: list):
    actual_result = get_longest_diverse_words(os.path.join(file))
    assert actual_result == expected_result


def test_get_rarest_char():
    actual_result = get_rarest_char(os.path.join(file))
    assert actual_result == "›"


def test_count_punctuation_chars():
    actual_result = count_punctuation_chars(os.path.join(file))
    assert actual_result == 5475


def test_count_non_ascii_chars():
    actual_result = count_non_ascii_chars(os.path.join(file))
    assert actual_result == 2972


def test_get_most_common_non_ascii_char():
    actual_result = get_most_common_non_ascii_char(os.path.join(file))
    assert actual_result == "ä"
