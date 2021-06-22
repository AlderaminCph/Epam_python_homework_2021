"""
Given a cell with "it's a fib sequence" from slideshow,
    please write function "check_fib", which accepts a Sequence of integers, and
    returns if the given sequence is a Fibonacci sequence
We guarantee, that the given sequence contain >= 0 integers inside.

"""


from typing import Sequence


def check_fibonacci(data: Sequence[int]) -> bool:
    """
    function that checks if the given sequence is a Fibonacci sequence
    returns Bool
    """
    if len(data) >= 3 and data[1] != 0:
        for i in range(2, len(data)):
            if data[i - 1] + data[i - 2] != data[i]:
                return False
        return True
    else:
        return False