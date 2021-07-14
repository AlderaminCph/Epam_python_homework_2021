"""
In previous homework task 4, you wrote a cache function that remembers other function output value. Modify it to be a parametrized decorator, so that the following code:

@cache(times=3)
def some_function():
    pass

Would give out cached value up to timess number only. Example:

@cache(times=2)
def f():
    return input('? ')   # careful with input() in python2, use raw_input() instead

>>> f()
? 1
'1'
>>> f()     # will remember previous value
'1'
>>> f()     # but use it up to two timess only
'1'
>>> f()
? 2
'2'

"""
from collections import defaultdict


def cache(times):
    """Cashe call to initial function up to times number only.
    (decorator).

    Args:
        times: the number of times to be cached
    Returns:
        function with cached values
    """

    def decorator(func):

        cache_dict = defaultdict(dict)


        def a_wrapper(*args, **kwargs):
            print("args ",*args)
            if args in cache_dict and cache_dict[args][1] != 0:
                cache_dict[args][1] -= 1
            if args not in cache_dict or (
                args in cache_dict and cache_dict[args][1] == 0
            ):
                cache_dict[args] = [func(*args, **kwargs), times]
            print('cache_dict ',cache_dict)
            return cache_dict[args][0]

        return a_wrapper

    return decorator
