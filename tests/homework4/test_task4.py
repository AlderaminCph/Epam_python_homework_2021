import pytest

from homework4.task4 import fizzbuzz


@pytest.mark.parametrize(
    ["n", "fizzbuzz_sequence"],
    [
        (1, ["1"]),
        (4, ["1", "2", "Fizz", "4"]),
        (0, []),
        (-1, []),
    ],
)
def test_fizzbuzz(n, fizzbuzz_sequence):
    our_result = fizzbuzz(n)
    assert our_result == our_result


def test_fizzbuzz_error():
    with pytest.raises(TypeError):
        fizzbuzz(1.5)
