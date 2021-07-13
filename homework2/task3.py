"""
Write a function that takes K lists as arguments and returns all possible
lists of K items where the first element is from the first list,
the second is from the second and so one.
You may assume that that every list contain at least one element
Example:
assert combinations([1, 2], [3, 4]) == [
    [1, 3],
    [1, 4],
    [2, 3],
    [2, 4],
]
"""
from typing import Any, List


def combinations(*args: List[Any]) -> List[List]:
    """Take K lists as arguments and returns all possible
    lists of K items where the first element is from the first list,
    the second is from the second and so one.

    Args:
        Input Lists
    Return:
        Output Lists
    """
    # for arg in args:
    if not args:
        raise ValueError("input list should be non-empty list")
    new_lists = [[]]
    for single_list in args:
        new_lists = [x + [y] for x in new_lists for y in single_list]
    return new_lists
