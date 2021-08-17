"""
Write a function that accepts another function as an argument. Then it
should return such a function, so the every call to initial one
should be cached.
def func(a, b):
    return (a ** b) ** 2

cache_func = cache(func)
some = 100, 200
val_1 = cache_func(*some)
val_2 = cache_func(*some)
assert val_1 is val_2
"""
from collections import defaultdict
from typing import Callable


def cache(func: Callable) -> Callable:
    """Cashe every call to initial function.
    (decorator).

    Args:
        input function
    Returns:
        such a function, so the every call to initial one
    should be cached.
    """
    cache_dict = defaultdict(dict)
    func_name = func.__name__

    def a_wrapper(args=None, kwargs=None):
        key = " ".join(str(i) for i in [func_name, str(args), str(kwargs)])
        if key not in cache_dict:
            cache_dict[key] = func(args, kwargs)
        return cache_dict[key]

    return a_wrapper