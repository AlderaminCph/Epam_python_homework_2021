"""
Classic task, a kind of walnut for you.

Given four lists A, B, C, D of integer values,
    compute how many tuples (i, j, k, l) there are such that A[i] + B[j] + C[k] + D[l] is zero.
We guarantee, that all A, B, C, D have same length of N where 0 ≤ N ≤ 1000.
"""
import itertools
from collections import defaultdict
from typing import List


def check_sum_of_four(a: List[int], b: List[int], c: List[int], d: List[int]) -> int:
    """Count the number of quadruplets with the zero sum.

    Args:
        a: list of integer vaules
        b: list of integer vaules
        c: list of integer vaules
        d: list of integer vaules
    Returns:
        number of tuples
    """
    counts = defaultdict(int)
    result = 0
    for (a_val, b_val) in itertools.product(a, b):
        counts[a_val + b_val] += 1
    for (c_val, d_val) in itertools.product(c, d):
        result += counts[-(c_val + d_val)]
    return result
