"""
Write a function that takes a number N as an input and returns N FizzBuzz numbers*
Write a doctest for that function.
Definition of done:
 - function is created
 - function is properly formatted
 - function has doctests
 - doctests are run with pytest command
You will learn:
 - the most common test task for developers
 - how to write doctests
 - how to run doctests
assert fizzbuzz(5) == ["1", "2", "fizz", "4", "buzz"]
* https://en.wikipedia.org/wiki/Fizz_buzz
** Энциклопедия профессора Фортрана page 14, 15, "Робот Фортран, чисть картошку!"
"""
from typing import List


def fizzbuzz(n: int) -> List[str]:
    """takes a number N as an input and returns N FizzBuzz numbers
    >>> fizzbuzz(5)
    ['1', '2', 'Fizz', '4', 'Buzz']
    >>> fizzbuzz(0)
    []
    >>> fizzbuzz(-5)
    []
    >>> fizzbuzz(5.5)
    Traceback (most recent call last):
        ...
    TypeError: 'float' object cannot be interpreted as an integer
    >>> fizzbuzz(15)
    ['1', '2', 'Fizz', '4', 'Buzz', 'Fizz', '7', '8', 'Fizz', 'Buzz', '11', 'Fizz', '13', '14', 'Fizz Buzz']

    """
    fizz_buzz = []
    if type(n) is not int:
        raise TypeError("'float' object cannot be interpreted as an integer")
    else:
        for i in range(1, n + 1):
            if i % 15 == 0:
                fizz_buzz.append("Fizz Buzz")
            elif i % 3 == 0:
                fizz_buzz.append("Fizz")
            elif i % 5 == 0:
                fizz_buzz.append("Buzz")
            else:
                fizz_buzz.append(str(i))
        return fizz_buzz


if __name__ == "__main__":
    import doctest

    doctest.testmod()
