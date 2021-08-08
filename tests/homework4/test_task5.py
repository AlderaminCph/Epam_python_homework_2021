import pytest

from homework4.task5 import fizzbuzz


@pytest.mark.parametrize(
    ["n", "fizzbuzz_sequence"],
    [
        (1, ["1"]),
        (4, ["1", "2", "fizz", "4", "buzz"]),
        (0, []),
        (-1, []),
    ],
)
def test_fizzbuzz(n, fizzbuzz_sequence):
    our_result = list(fizzbuzz(n))
    assert our_result == our_result
