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


def my_range_function(iterable_values, arg1: str, arg2=None, step=1):
    """Return an object that produces a sequence of iterable values from start (inclusive)
    to stop (exclusive) by step.
    range(i, j) produces i, i+1, i+2, ..., j-1.
    When step is given, it specifies the increment (or decrement).

    Args:
        iterable_values:
        arg1: end value (if only two arguments) or first value (if 3 or more arguments)
        arg2: first value (if step is negative) or end value (if step is positive)
        step: specifies the increment (positive) or decrement (negative)
    Returns:
        Sequence of iterable values from start to stop by step
    """
    list_of_values = list(iterable_values)
    if step == 0:
        raise ValueError("step must be non-zero")
    if arg2 and arg2 not in list_of_values or arg1 not in list_of_values:
        raise ValueError("arguments are beyond limits of iterable values")
    if arg2:
        start = arg1
        stop = arg2
        index_start = list_of_values.index(start)
    else:
        index_start = 0
        stop = arg1
    index_stop = list_of_values.index(stop)
    print("index_start = ", index_start)
    print("index_stop = ", index_stop)
    result = list(iterable_values[index_start:index_stop:step])
    return result
