"""
Given a list of integers numbers "nums".
You need to find a sub-array with length less equal to "k", with maximal sum.
The written function should return the sum of this sub-array.
Examples:
    nums = [1, 3, -1, -3, 5, 3, 6, 7], k = 3
    result = 16
"""
from typing import List


def find_maximal_subarray_sum(nums: List[int], k: int) -> int:
    """
    function that finds largest subarray sum
    with at-least k elements in it.
    Returns maximum sum of a subarray
    with at-least k elements.
    """
    if len(nums) == 0 or k <= 0 or k > len(nums):
        return "Invalid input: k should be nonzero and less than nonzero array size."
    summ = 0
    for i in range(k):
        summ += nums[i]
    max_sum = summ
    start = 0
    for j in range(k, len(nums)):
        summ = summ + nums[j] - nums[start]
        start += 1
        if summ > max_sum:
            max_sum = summ
    return max_sum
