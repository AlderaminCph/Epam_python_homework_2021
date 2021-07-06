"""
Given an array of size n, find the most common and the least common elements.
The most common element is the element that appears more than n // 2 times.
The least common element is the element that appears fewer than other.
You may assume that the array is non-empty and the most common element
always exist in the array.
Example 1:
Input: [3,2,3]
Output: 3, 2
Example 2:
Input: [2,2,1,1,1,2,2]
Output: 2, 1
"""
from typing import List, Tuple


def major_and_minor_elem(inp: List) -> Tuple[int, int]:
    """Find the most common and the least common elements.

    Args:
        inp: List of integers
    Returns:
        tuple containing most common and least common elements
    """
    if not inp:
        raise ValueError("input list should be non-empty list.")
    counter_elements = {}
    for i in inp:
        if i in counter_elements:
            counter_elements[i] += 1
        else:
            counter_elements[i] = 1
    sort_counter_elements = sorted(counter_elements.items(), key=lambda item: item[1])
    return (sort_counter_elements[-1][0], sort_counter_elements[0][0])
