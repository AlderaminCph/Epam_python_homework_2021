"""
Some of the functions have a bit cumbersome behavior when we deal with
positional and keyword arguments.
Write a function that accept any iterable of unique values and then
it behaves as range function:
import string
assert = custom_range(string.ascii_lowercase, 'g') == ['a', 'b', 'c', 'd', 'e', 'f']
assert = custom_range(string.ascii_lowercase, 'g', 'p') == ['g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o']
assert = custom_range(string.ascii_lowercase, 'p', 'g', -2) == ['p', 'n', 'l', 'j', 'h']
"""
import string


def my_range_function(iterable_values, stop: str, start=None, step=1):
    """Return an object that produces a sequence of iterable values from start (inclusive)
    to stop (exclusive) by step.
    range(i, j) produces i, i+1, i+2, ..., j-1.
    When step is given, it specifies the increment (or decrement).

    Args:
        iterable_values:
        stop: end value
        start: first value
        step: specifies the increment (positive) or decrement (negative)
    Returns:
        Sequence of iterable values from start to stop by step
    """
    if step == 0:
        raise ValueError("step must be non-zero")
    list_of_values = list(iterable_values)
    if start is None:
        return list(iterable_values[0 : list_of_values.index(stop) : step])
    elif step < 0:
        start, stop = stop, start
        return list(
            iterable_values[
                list_of_values.index(start) : list_of_values.index(stop) : step
            ]
        )
    else:
        start, stop = stop, start
        return list(
            iterable_values[
                list_of_values.index(start) : list_of_values.index(stop) : step
            ]
        )
