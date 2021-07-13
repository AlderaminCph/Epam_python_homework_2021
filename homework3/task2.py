'''
Here's a not very efficient calculation function that calculates something important:

import time
import struct
import random
import hashlib

def slow_calculate(value):
    """Some weird voodoo magic calculations"""
    time.sleep(random.randint(1,3))
    data = hashlib.md5(str(value).encode()).digest()
    return sum(struct.unpack('<' + 'B' * len(data), data))

Calculate total sum of slow_calculate() of all numbers starting from 0 to 500. Calculation time should not take more than a minute. Use functional capabilities of multiprocessing module. You are not allowed to modify slow_calculate function.
'''
import hashlib
import random
import struct
import time
from multiprocessing import Pool


def slow_calculate(value):
    """Some weird voodoo magic calculations"""
    time.sleep(random.randint(1, 3))
    data = hashlib.md5(str(value).encode()).digest()
    return sum(struct.unpack("<" + "B" * len(data), data))


def my_calculation(numbers, func):
    """Calculate total sum of slow_calculate() of all numbers starting from 0 to 500.

    Args:
        numbers: values to give to slow_calculate
        func: function
    Returns:
        total sum
    """
    pool = Pool(60)
    return sum(pool.map(func, numbers))


if __name__ == "__main__":
    print(my_calculation(list(range(0, 501)), slow_calculate))
